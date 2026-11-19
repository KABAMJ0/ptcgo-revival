import os
import importlib.util
import json
import logging
import sys
from typing import Dict, List
from ptcgo.game.models.card import Card, PokemonCard
from ptcgo.game.attributes import AttrID, CardType

# Printed ability types ("Poké-Power", "Poké-Body", "Ability") live only in the
# set JSON beside the scripts, and a script never sets AbilityTypes itself, so a
# card that has to tell a Poké-Power from a modern Ability reads them here.
_PRINTED_ABILITY_TYPES: Dict[str, Dict[int, Dict[str, str]]] = {}


def _printed_abilities_for_set(set_code: str) -> Dict[int, Dict[str, str]]:
    """collector number -> {printed ability title: printed type} for one set."""
    cached = _PRINTED_ABILITY_TYPES.get(set_code)
    if cached is not None:
        return cached
    cached = {}
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), set_code)
    path = None
    if os.path.isdir(directory):
        wanted = f"{set_code.lower()}.json"
        for name in sorted(os.listdir(directory)):
            if name.lower() == wanted:
                path = os.path.join(directory, name)
                break
    if path:
        try:
            with open(path, encoding="utf-8") as handle:
                data = json.load(handle)
            cards = data if isinstance(data, list) else data.get("cards", [])
            for entry in cards:
                named = {ability.get("name") or "": ability.get("type") or ""
                         for ability in (entry.get("abilities") or [])}
                if named:
                    cached[int(entry.get("number", -1))] = named
        except (OSError, ValueError, TypeError):
            cached = {}
    _PRINTED_ABILITY_TYPES[set_code] = cached
    return cached


def printed_ability_type(card_def, title: str) -> str:
    """The printed type of the ability called `title` on `card_def`.

    "Poké-Power", "Poké-Body", "Ability" and so on live only in the set JSON
    beside the scripts; no script sets `AbilityTypes` itself, so a card that has
    to tell a Poké-Power from a modern Ability reads it here. Matching is by
    title because a script adds Attacks to `abilities` too, which the printed
    list does not carry. Empty when the set or the title is unknown."""
    set_code = getattr(card_def, "set_code", None)
    number = getattr(card_def, "collector_number", None)
    if not set_code or number is None or not title:
        return ""
    return _printed_abilities_for_set(set_code).get(int(number), {}).get(title, "")


class ScriptLoader:
    """Dynamically loads card definition scripts from the filesystem."""
    def __init__(self, scripts_dir: str):
        self.scripts_dir = os.path.abspath(scripts_dir)
        self.cards: List[Card] = []
        self.cards_by_guid: Dict[str, Card] = {}
        self.cards_by_key: Dict[str, Card] = {}
        # script filename stem (e.g. "Watchog_79") -> archetype GUID
        self.cards_by_stem: Dict[str, str] = {}
        self.definitions = {}
        self.last_errors = []
        # Per-set effect coverage (the admin Coverage view reads it): how many
        # attack/ability entries exist and how many still carry the
        # `unimplemented` marker.
        self.coverage = {}

    def load_all(self, force=False):
        """Loads all card scripts once; cached thereafter unless force=True.

        Re-running scripts rebuilds effect registries (ABILITIES_BY_ID etc.)
        and blocks the event loop ~1s, so hot paths must hit the cache.
        """
        if self.cards and not force:
            return self.cards
        self.cards = []
        self.cards_by_guid = {}
        self.cards_by_key = {}
        self.cards_by_stem = {}
        self.definitions = {}
        self.last_errors = []
        self.coverage = {}

        logging.info(f"[Scripts] Loading card scripts from {self.scripts_dir}...")
        
        for root, dirs, files in os.walk(self.scripts_dir):
            dirs.sort()
            for file in sorted(files):
                if file.endswith(".py") and file != "__init__.py":
                    file_path = os.path.join(root, file)
                    self._load_script(file_path)

        resolved = {}
        for reference in self.definitions:
            try:
                self._resolve(reference, resolved, [])
            except Exception as e:
                error = f"{reference}: {e}"
                self.last_errors.append(error)
                logging.error("[Scripts] Failed to resolve card %s", error)

        invalid = self._resolve_legends(resolved) | self._resolve_vunions(resolved)
        # Admin overrides (card_overrides table) land on resolved definitions before
        # wording patterns bind, so an overridden effect is never re-bound.
        from ptcgo.game.content import card_overrides
        card_overrides.apply_at_load(
            {ref: d for ref, d in resolved.items() if ref not in invalid})
        # Wording-driven effects bind here, once, after every definition is
        # resolved: card_effects imports this module indirectly, so the
        # resolver cannot be imported at module scope.
        from ptcgo.game.card_effects import patterns
        self.pattern_bound = 0
        for reference, card_def in resolved.items():
            if reference not in invalid and not getattr(card_def, "runtime_only", False):
                try:
                    self.pattern_bound += patterns.bind_definition(card_def)
                    self._add_card(reference, card_def)
                    self._count_coverage(reference, card_def)
                except Exception as error:
                    self.last_errors.append(f"{reference}: {error}")
                    logging.error("[Scripts] Failed to publish card %s: %s", reference, error)
        
        logging.info(f"[Scripts] Successfully loaded {len(self.cards)} card scripts.")
        return self.cards

    def _resolve_legends(self, resolved):
        """Validate references and complete pairs before publishing physical halves."""
        invalid = set()
        pairs = {}
        for reference, definition in resolved.items():
            if not hasattr(definition, "resolve_legend"):
                continue
            try:
                if definition.legend not in resolved:
                    raise ValueError(f"Missing LEGEND definition: {definition.legend}")
                definition.resolve_legend(resolved[definition.legend])
                pairs.setdefault(definition.legend, []).append((reference, definition))
            except (ValueError, TypeError) as error:
                invalid.add(reference)
                self.last_errors.append(f"{reference}: {error}")
        for reference, halves in pairs.items():
            problem = None
            if {half.half for _, half in halves} != {"top", "bottom"}:
                problem = "LEGEND requires both top and bottom printings"
            elif len({half.guid.lower() for _, half in halves}) != len(halves):
                problem = "LEGEND printings must have distinct GUIDs"
            if problem:
                for path, half in halves:
                    half.legend_definition = None
                    invalid.add(path)
                self.last_errors.append(f"{reference}: {problem}")
        return invalid

    def _resolve_vunions(self, resolved):
        """Bind pieces to their combined Pokemon; a set missing any position publishes none of it."""
        invalid = set()
        groups = {}
        for reference, definition in resolved.items():
            if not hasattr(definition, "resolve_vunion"):
                continue
            try:
                if definition.vunion not in resolved:
                    raise ValueError(f"Missing V-UNION definition: {definition.vunion}")
                definition.resolve_vunion(resolved[definition.vunion])
                groups.setdefault(definition.vunion, []).append((reference, definition))
            except (ValueError, TypeError) as error:
                invalid.add(reference)
                self.last_errors.append(f"{reference}: {error}")
        for reference, pieces in groups.items():
            problem = None
            slots = [piece.piece for _, piece in pieces]
            if sorted(slots) != list(range(4)):
                problem = "V-UNION requires exactly one printing of each of the 4 pieces"
            elif len({piece.guid.lower() for _, piece in pieces}) != len(pieces):
                problem = "V-UNION printings must have distinct GUIDs"
            if problem:
                for path, piece in pieces:
                    piece.vunion_definition = None
                    invalid.add(path)
                self.last_errors.append(f"{reference}: {problem}")
                continue
            resolved[reference].bind_pieces([piece for _, piece in pieces])
        return invalid

    def _resolve(self, reference, resolved, chain):
        """Resolve parent definitions independently of filesystem order."""
        if reference in resolved:
            return resolved[reference]
        if reference in chain:
            raise ValueError("Reprint inheritance cycle: " + " -> ".join(chain + [reference]))
        if reference not in self.definitions:
            raise ValueError(f"Missing reprint parent: {reference}")
        definition = self.definitions[reference]
        if getattr(definition, "inherits", None) is not None:
            parent = self._resolve(definition.inherits, resolved, chain + [reference])
            definition = definition.resolve(parent)
        resolved[reference] = definition
        return definition

    def _count_coverage(self, reference, card_def):
        """Tallies one published card's attack/ability entries by how they run."""
        from ptcgo.game.data_utils import unimplemented
        row = self.coverage.setdefault(reference.split("/", 1)[0], {
            "cards": 0, "entries": 0, "stubbed": 0,
            "wording": 0, "scripted": 0, "plain": 0,
            "trainer_effects": 0, "trainer_stubbed": 0,
        })
        row["cards"] += 1
        # A Trainer's play effect is a card-level body, not an attack/ability entry, so it
        # is tallied beside the entries rather than inside them.
        from ptcgo.game.data_utils import TrainerCardDef
        if isinstance(card_def, TrainerCardDef):
            row["trainer_effects"] += 1
            row["trainer_stubbed"] += int(card_def.effect is unimplemented)
        for ability in getattr(card_def, "abilities", None) or []:
            row["entries"] += 1
            effect = getattr(ability, "effect", None)
            # A wording pattern can bind an Ability as a passive and leave its effect
            # as the marker, so the marker alone is a stub only with no passive.
            if effect is unimplemented and getattr(ability, "passive", None) is None:
                row["stubbed"] += 1
            elif str(getattr(ability, "effect_source", "") or "").startswith("pattern:"):
                row["wording"] += 1
            elif (effect is not None or getattr(ability, "passive", None) is not None
                  or getattr(ability, "trigger", None) or getattr(ability, "activation", None)):
                row["scripted"] += 1
            else:
                row["plain"] += 1

    def _add_card(self, reference, card_def):
        """Publish a resolved definition as a server card model."""
        archetype = card_def.to_archetype_dict()
        guid, key, attrs = archetype["guid"], archetype["key"], archetype["attributes"]
        c_type = attrs.get(str(AttrID.CARD_TYPE.value), {}).get("value", CardType.UNSET)
        model = PokemonCard if c_type == CardType.POKEMON else Card
        card = model(guid, key, attrs, archetype.get("display_name"),
                     archetype.get("searchable_by", []), getattr(card_def, "subtypes", []))
        # A GUID is a card's identity, and the client crashes at login when it meets
        # two archetypes with one identity ("An item with the same key has already
        # been added"). This dict used to overwrite the first card silently, so a
        # copy-pasted script shipped and hung the client at 63%. Refuse instead.
        existing = self.cards_by_guid.get(guid)
        if existing is not None:
            clash = (f"{reference}: archetype GUID {guid} is already used by "
                     f"{getattr(existing, 'display_name', '?')} ({existing.key})")
            self.last_errors.append(clash)
            logging.error("[Scripts] Duplicate archetype GUID %s", clash)
            return
        self.cards.append(card)
        self.cards_by_guid[guid] = card
        self.cards_by_key[key] = card
        self.cards_by_stem[reference.rsplit("/", 1)[-1]] = guid

    def _load_script(self, file_path: str):
        """Loads a single card script."""
        try:
            # Create a unique module name based on the relative path
            rel_path = os.path.relpath(file_path, self.scripts_dir)
            module_name = "card_script_" + rel_path.replace(os.path.sep, "_").replace(".py", "")
            
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                logging.error(f"[Scripts] Could not create spec or loader for {file_path}")
                return

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'card'):
                reference = os.path.splitext(rel_path)[0].replace(os.path.sep, "/")
                self.definitions[reference] = module.card
            else:
                logging.warning(f"[Scripts] Script {file_path} does not define a 'card' object.")
                
        except Exception as e:
            self.last_errors.append(f"{file_path}: {e}")
            logging.error(f"[Scripts] Failed to load script {file_path}: {e}")

# Global loader instance
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__))
loader = ScriptLoader(SCRIPTS_DIR)
