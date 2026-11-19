"""Admin card-behaviour overrides: a persisted table applied at load time.

Card scripts are imported once at boot, so editing one on the live checkout either
needs a restart or silently does nothing. Instead an operator writes a row to the
`card_overrides` table (keyed by card GUID plus attack title) and the loader
applies it after every definition is resolved and before wording patterns bind.

An override can express exactly four things about an *attack*:

- `damage`: the printed damage the engine reads (`Attack.damage`);
- `damage_operator`: the "", "+", "x" or "-" suffix the client shows next to it;
- `cost`: the Energy cost, by client type name;
- `effect`: `null` (printed damage only) or a named factory from an allow-listed
  module called with JSON keyword arguments.

Anything else is refused with a reason rather than approximated: Abilities
(they carry triggers, passives and activation rules), factories that take a
function (`then=`, `also=`, `count_fn`...), `*args` factories, dict-valued
parameters, and any factory call that does not produce an attack coroutine.

Reload path: rows take effect at the next boot automatically. `apply_live()`
re-applies the whole table in place on the running process; it is what the admin
"Apply now" button calls.
"""
import importlib
import inspect
import logging
import os
import threading
from typing import Any, Dict, List, Optional, Tuple

from ptcgo.game.attributes import AttrID, CLIENT_POKEMON_TYPE_NAMES, PokemonTypes, SpecialConditions

FACTORY_MODULES = ("attacks_common", "support_common")
DAMAGE_OPERATORS = ("", "+", "x", "-")
MAX_DAMAGE = 9990
MAX_COST = 10

TYPE_BY_NAME = {name: ptype for ptype, name in CLIENT_POKEMON_TYPE_NAMES.items()
                if ptype != PokemonTypes.NO_COLOR}
CONDITION_BY_NAME = {c.name.capitalize(): c for c in SpecialConditions if c != SpecialConditions.UNSET}

# Parameters that hold a game enum: JSON carries the enum's name.
ENUM_PARAMS = {
    "condition": CONDITION_BY_NAME,
    "self_condition": CONDITION_BY_NAME,
    "energy_type": TYPE_BY_NAME,
}
# Required, unannotated parameters that the factories in FACTORY_MODULES use as
# plain integers. Anything required and not listed here is refused.
INT_PARAM_NAMES = {"amount", "count", "per", "bonus", "self_damage", "damage",
                   "per_energy", "required", "picks", "mill_count", "coins"}

_lock = threading.Lock()
# (guid_lower, title) -> True for every attack currently carrying an override
_applied: Dict[Tuple[str, str], bool] = {}
# Result of the last application, for the admin view: [{guid,title,status,error}]
report: List[dict] = []
last_applied_at: Optional[float] = None
last_mode: str = ""


class OverrideError(ValueError):
    """The spec cannot be expressed; the message says why."""


# ----------------------------------------------------------------- factories

def _module(name):
    if name not in FACTORY_MODULES:
        raise OverrideError(f"module '{name}' is not on the override allow-list")
    return importlib.import_module(f"ptcgo.game.card_effects.{name}")


def _param_kind(param) -> Optional[str]:
    """'int' | 'bool' | 'str' | 'int?' | 'enum:<name>' | None (inexpressible)."""
    if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
        return None
    if param.name in ENUM_PARAMS:
        return f"enum:{param.name}"
    annotation = param.annotation
    text = annotation if isinstance(annotation, str) else getattr(annotation, "__name__", None) or str(annotation)
    text = str(text).replace("typing.", "")
    if "Callable" in text:
        return None
    default = param.default
    if default is not inspect.Parameter.empty:
        if callable(default):
            return None
        if isinstance(default, bool):
            return "bool"
        if isinstance(default, int):
            return "int"
        if isinstance(default, str):
            return "str"
        if default is None:
            return "int?" if text in ("Optional[int]", "int | None", "Union[int, NoneType]") else None
        return None
    if text in ("int",) or param.name in INT_PARAM_NAMES:
        return "int"
    if text == "bool":
        return "bool"
    if text == "str":
        return "str"
    return None


def describe_factory(module_name, factory_name) -> Optional[dict]:
    """The factory's expressible parameters, or None when it is not an attack factory."""
    try:
        module = _module(module_name)
    except (OverrideError, ImportError):
        return None
    fn = getattr(module, factory_name, None)
    if not inspect.isfunction(fn) or fn.__module__ != module.__name__ or factory_name.startswith("_"):
        return None
    # support_common also holds Trainer bodies, which expect a trainer context.
    if module_name == "support_common" and "attack" not in factory_name:
        return None
    try:
        source = inspect.getsource(fn)
    except (OSError, TypeError):
        return None
    if "async def" not in source:
        return None
    params, hidden = [], []
    for p in inspect.signature(fn).parameters.values():
        kind = _param_kind(p)
        required = p.default is inspect.Parameter.empty
        if kind is None:
            if required or p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
                return None
            hidden.append(p.name)
            continue
        entry = {"name": p.name, "type": kind, "required": required}
        if not required:
            entry["default"] = p.default.name if hasattr(p.default, "name") else p.default
        if kind.startswith("enum:"):
            entry["choices"] = sorted(ENUM_PARAMS[p.name])
        params.append(entry)
    doc = (inspect.getdoc(fn) or "").strip().split("\n\n")[0]
    return {"module": module_name, "factory": factory_name, "params": params,
            "not_settable": hidden, "doc": doc}


_CATALOG = None


def factory_catalog() -> List[dict]:
    global _CATALOG
    if _CATALOG is None:
        out = []
        for module_name in FACTORY_MODULES:
            module = _module(module_name)
            for name, fn in sorted(vars(module).items()):
                if inspect.isfunction(fn):
                    info = describe_factory(module_name, name)
                    if info:
                        out.append(info)
        _CATALOG = out
    return _CATALOG


def _coerce(param_info, value):
    kind, name = param_info["type"], param_info["name"]
    if kind.startswith("enum:"):
        if value is None and not param_info["required"]:
            return None
        table = ENUM_PARAMS[name]
        if value not in table:
            raise OverrideError(f"{name} must be one of {', '.join(sorted(table))}")
        return table[value]
    if kind == "bool":
        if not isinstance(value, bool):
            raise OverrideError(f"{name} must be true or false")
        return value
    if kind == "str":
        if not isinstance(value, str) or len(value) > 200:
            raise OverrideError(f"{name} must be a short string")
        return value
    if kind == "int?" and value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise OverrideError(f"{name} must be a whole number")
    if not -MAX_DAMAGE <= value <= MAX_DAMAGE:
        raise OverrideError(f"{name} is out of range")
    return value


def build_effect(effect_spec):
    """(effect_callable, normalized_spec). Raises OverrideError."""
    if not isinstance(effect_spec, dict):
        raise OverrideError("effect must be null or {module, factory, kwargs}")
    unknown = set(effect_spec) - {"module", "factory", "kwargs"}
    if unknown:
        raise OverrideError(f"effect has unknown keys: {', '.join(sorted(unknown))}")
    module_name = effect_spec.get("module") or "attacks_common"
    factory_name = str(effect_spec.get("factory") or "")
    info = describe_factory(module_name, factory_name)
    if info is None:
        raise OverrideError(f"{module_name}.{factory_name} is not an attack factory the override can call")
    kwargs = effect_spec.get("kwargs") or {}
    if not isinstance(kwargs, dict):
        raise OverrideError("kwargs must be an object")
    by_name = {p["name"]: p for p in info["params"]}
    for name in kwargs:
        if name in info["not_settable"]:
            raise OverrideError(f"{factory_name}({name}=...) takes a function or a structured value; "
                                "the override cannot express it")
        if name not in by_name:
            raise OverrideError(f"{factory_name} has no parameter '{name}'")
    call = {}
    for p in info["params"]:
        if p["name"] in kwargs:
            call[p["name"]] = _coerce(p, kwargs[p["name"]])
        elif p["required"]:
            raise OverrideError(f"{factory_name} needs '{p['name']}'")
    try:
        effect = getattr(_module(module_name), factory_name)(**call)
    except Exception as exc:
        raise OverrideError(f"{factory_name} refused those arguments: {exc}") from exc
    if not inspect.iscoroutinefunction(effect):
        raise OverrideError(f"{factory_name} does not build an attack effect")
    return effect, {"module": module_name, "factory": factory_name,
                    "kwargs": {k: kwargs[k] for k in sorted(kwargs)}}


# ------------------------------------------------------------ validation

def find_attack(definition, title):
    from ptcgo.game.data_utils import Attack
    for ability in getattr(definition, "abilities", None) or []:
        if ability.title == title:
            if not isinstance(ability, Attack):
                raise OverrideError(f"'{title}' is an Ability; abilities carry triggers, passives and "
                                    "activation rules the override cannot express")
            return ability
    raise OverrideError(f"card has no attack titled '{title}'")


def normalize_spec(spec) -> dict:
    """Checks the shape of a spec without building it. Raises OverrideError."""
    if not isinstance(spec, dict) or not spec:
        raise OverrideError("spec must be a non-empty object")
    unknown = set(spec) - {"damage", "damage_operator", "cost", "effect"}
    if unknown:
        raise OverrideError(f"cannot override: {', '.join(sorted(unknown))}")
    out = {}
    if "damage" in spec:
        damage = spec["damage"]
        if isinstance(damage, bool) or not isinstance(damage, int) or not 0 <= damage <= MAX_DAMAGE:
            raise OverrideError(f"damage must be a whole number from 0 to {MAX_DAMAGE}")
        out["damage"] = damage
    if "damage_operator" in spec:
        if spec["damage_operator"] not in DAMAGE_OPERATORS:
            raise OverrideError('damage_operator must be "", "+", "x" or "-"')
        out["damage_operator"] = spec["damage_operator"]
    if "cost" in spec:
        cost = spec["cost"]
        if not isinstance(cost, dict):
            raise OverrideError("cost must be an object of {TypeName: count}")
        clean = {}
        for name, n in cost.items():
            if name not in TYPE_BY_NAME:
                raise OverrideError(f"unknown energy type '{name}'")
            if isinstance(n, bool) or not isinstance(n, int) or not 0 <= n <= MAX_COST:
                raise OverrideError(f"{name} cost must be 0..{MAX_COST}")
            if n:
                clean[name] = n
        if sum(clean.values()) > MAX_COST:
            raise OverrideError(f"total cost above {MAX_COST}")
        out["cost"] = clean
    if "effect" in spec:
        out["effect"] = None if spec["effect"] is None else build_effect(spec["effect"])[1]
    return out


def validate(definition, title, spec) -> dict:
    """Normalized spec for this card's attack. Raises OverrideError."""
    if definition is None:
        raise OverrideError("no loaded card has that GUID")
    find_attack(definition, title)
    return normalize_spec(spec)


# ------------------------------------------------------------- application

def _snapshot(ability):
    if not hasattr(ability, "_admin_original"):
        ability._admin_original = {
            "damage": ability.damage,
            "damage_operator": ability.damage_operator,
            "cost": dict(ability.cost),
            "effect": ability.effect,
            "effect_source": getattr(ability, "effect_source", None),
        }


def _apply_one(definition, title, spec):
    ability = find_attack(definition, title)
    normalized = normalize_spec(spec)
    effect = None
    if normalized.get("effect"):
        effect, _ = build_effect(normalized["effect"])
    _snapshot(ability)
    if "damage" in normalized:
        ability.damage = normalized["damage"]
    if "damage_operator" in normalized:
        ability.damage_operator = normalized["damage_operator"]
    if "cost" in normalized:
        ability.cost = {TYPE_BY_NAME[name]: n for name, n in normalized["cost"].items()}
    if "effect" in normalized:
        ability.effect = effect
        source = normalized["effect"]["factory"] if normalized["effect"] else "vanilla"
        ability.effect_source = f"admin:{source}"
    return ability


def _revert(ability, own_name=None):
    original = getattr(ability, "_admin_original", None)
    if original is None:
        return
    ability.damage = original["damage"]
    ability.damage_operator = original["damage_operator"]
    ability.cost = dict(original["cost"])
    ability.effect = original["effect"]
    ability.effect_source = original["effect_source"]
    del ability._admin_original
    from ptcgo.game.data_utils import unimplemented
    if ability.effect is unimplemented:
        from ptcgo.game.card_effects import patterns
        patterns.bind(ability, own_name)


def refresh_ability_attribute(definition):
    """Re-serializes PIE_ABILITIES (what the client shows and the engine costs from)."""
    from ptcgo.game.content.definitions import with_sort_order
    key = str(AttrID.PIE_ABILITIES.value)
    if key not in definition.extra_attributes:
        return None
    import json
    value = {"type": "json", "value": json.dumps(with_sort_order([a.to_dict() for a in definition.abilities]))}
    definition.extra_attributes[key] = value
    return value


def _table_ready(table):
    from ptcgo import config
    from ptcgo.database import connection
    if not config.DATABASE_URL and not os.path.exists(connection.DB_PATH):
        return False
    from sqlalchemy import inspect as sa_inspect
    return sa_inspect(connection.engine).has_table(table)


def load_rows() -> List[dict]:
    """Enabled override rows. Empty when the database or table does not exist yet
    (the loader runs at import, before the server's create_all)."""
    if not _table_ready("card_overrides"):
        return []
    from ptcgo.database import db_session, CardOverride
    with db_session() as session:
        return [{"guid": r.archetype_id.lower(), "title": r.title, "spec": r.spec_json}
                for r in session.query(CardOverride).filter_by(enabled=True).order_by(CardOverride.id)]


def _apply_rows(rows, definitions_by_guid):
    results, touched = [], {}
    for row in rows:
        definition = definitions_by_guid.get(row["guid"])
        entry = {"guid": row["guid"], "title": row["title"]}
        try:
            if definition is None:
                raise OverrideError("no loaded card has that GUID")
            _apply_one(definition, row["title"], row["spec"])
            _applied[(row["guid"], row["title"])] = True
            touched[row["guid"]] = definition
            entry["status"] = "applied"
        except OverrideError as exc:
            entry.update(status="refused", error=str(exc))
        except Exception as exc:
            logging.error("[Overrides] %s / %s failed: %s", row["guid"], row["title"], exc)
            entry.update(status="failed", error=str(exc))
        results.append(entry)
    return results, touched


def apply_at_load(resolved: Dict[str, Any]):
    """Loader hook: after resolution, before pattern binding. Never raises."""
    global report, last_applied_at, last_mode
    import time
    with _lock:
        _applied.clear()
        try:
            rows = load_rows()
        except Exception as exc:
            logging.error("[Overrides] could not read card_overrides: %s", exc)
            report, last_mode = [{"status": "failed", "error": f"table unreadable: {exc}"}], "boot"
            return
        if not rows:
            report, last_mode, last_applied_at = [], "boot", time.time()
            return
        by_guid = {getattr(d, "guid", "").lower(): d for d in resolved.values() if getattr(d, "guid", None)}
        results, touched = _apply_rows(rows, by_guid)
        for definition in touched.values():
            refresh_ability_attribute(definition)
        report, last_mode, last_applied_at = results, "boot", time.time()
        logging.info("[Overrides] %d applied, %d refused at load",
                     sum(r["status"] == "applied" for r in results),
                     sum(r["status"] != "applied" for r in results))


def apply_live() -> List[dict]:
    """Re-applies the table on the running server: reverts every override this
    process applied, applies the current enabled rows, re-serializes the cards'
    PIE_ABILITIES and drops the cached archetype payloads.

    The attack objects are shared with running matches: a damage or effect change
    lands on the next use of that attack, including in matches already in progress.
    A cost change lands in matches that start afterwards (entities copy the cost
    when the match builds them)."""
    global report, last_applied_at, last_mode
    import time
    from ptcgo.game.content.definitions import CARD_DEFS_BY_GUID
    from ptcgo.game.scripts.cards import loader as card_loader
    rows = load_rows()
    with _lock:
        touched = {}
        for guid, title in list(_applied):
            definition = CARD_DEFS_BY_GUID.get(guid)
            if definition is None:
                continue
            for ability in getattr(definition, "abilities", None) or []:
                if ability.title == title:
                    _revert(ability, getattr(definition, "display_name", None))
            touched[guid] = definition
        _applied.clear()
        results, applied_to = _apply_rows(rows, CARD_DEFS_BY_GUID)
        touched.update(applied_to)
        for definition in touched.values():
            value = refresh_ability_attribute(definition)
            card = card_loader.cards_by_guid.get(definition.guid)
            if card is not None and value is not None:
                card.attributes[str(AttrID.PIE_ABILITIES.value)] = value
        report, last_mode, last_applied_at = results, "live", time.time()
    try:
        from ptcgo.packets.handlers import data_sync
        data_sync._clear_derived_caches()
    except Exception as exc:
        logging.error("[Overrides] could not clear archetype caches: %s", exc)
    return results


def describe_attack(ability) -> dict:
    """What the admin view shows for one attack or ability."""
    from ptcgo.game.data_utils import Attack, unimplemented
    is_attack = isinstance(ability, Attack)
    effect = getattr(ability, "effect", None)
    source = getattr(ability, "effect_source", None) or ""
    if effect is unimplemented:
        how = "unimplemented"
    elif source.startswith("admin:"):
        how = source
    elif source.startswith("pattern:"):
        how = source
    elif effect is None and is_attack:
        how = "vanilla"
    else:
        how = "scripted"
    out = {"title": ability.title, "text": ability.game_text, "kind": "attack" if is_attack else "ability",
           "effect": how, "overridden": hasattr(ability, "_admin_original"),
           "overridable": is_attack}
    if is_attack:
        out.update(damage=ability.damage, damage_operator=ability.damage_operator,
                   cost={CLIENT_POKEMON_TYPE_NAMES[k]: v for k, v in ability.cost.items()})
        original = getattr(ability, "_admin_original", None)
        if original:
            out["original"] = {
                "damage": original["damage"], "damage_operator": original["damage_operator"],
                "cost": {CLIENT_POKEMON_TYPE_NAMES[k]: v for k, v in original["cost"].items()},
            }
    else:
        out["refusal"] = "Abilities carry triggers, passives and activation rules the override cannot express."
    return out
