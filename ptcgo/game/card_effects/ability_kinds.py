"""Restore each ability's PRINTED kind (Ability / Poké-Body / Poké-Power /
Pokémon Power) at load.

Every non-attack ability in the corpus loads with `ability_type == POKE_ABILITY`,
because no card script passes `ability_type=` and the constructor default
flattens them. The distinction is printed in the set JSON beside the script and
nothing else carries it, so a Poké-Body and a Poké-Power are indistinguishable at
play time -- which is not cosmetic: the kind decides when an ability may be used,
whether a card that shuts off "Poké-Powers" reaches it, and what an ability that
names the other kind may target.

Reading the kind from the JSON is already what `has_poke_power` does per card;
this applies the same reading once, at load, so every consumer sees the right
value instead of each one remembering to ask the JSON.
"""
from typing import Optional

from ptcgo.game.attributes import AbilityTypes
from ptcgo.game.data_utils import Attack

# Printed spellings, normalised: the JSON carries "Poké-Power", "Poké-POWER" and
# the vintage "Pokémon Power" for the same kind.
_KIND_BY_PRINTED = {
    "ability": AbilityTypes.POKE_ABILITY,
    "poke-body": AbilityTypes.POKE_BODY,
    "pokemon body": AbilityTypes.POKE_BODY,
    "poke-power": AbilityTypes.POKE_POWER,
    "pokemon power": AbilityTypes.POKE_POWER,
    "ancient trait": AbilityTypes.ANCIENT_TRAIT,
    "technical machine": AbilityTypes.TECHNICAL_MACHINE,
}


def kind_of(printed: str) -> Optional[AbilityTypes]:
    """The AbilityTypes value a printed kind names, or None when unknown."""
    text = (printed or "").strip().lower()
    text = (text.replace("\u00e9", "e").replace("\u00c9", "E"))
    text = text.encode("ascii", "ignore").decode()
    return _KIND_BY_PRINTED.get(text)


def apply_printed_kinds(definition) -> int:
    """Set each non-attack ability's `ability_type` from its printed kind.
    Returns how many changed."""
    from ptcgo.game.scripts.cards import printed_ability_type

    changed = 0
    for ability in getattr(definition, "abilities", []) or []:
        if isinstance(ability, Attack):
            continue
        kind = kind_of(printed_ability_type(
            definition, getattr(ability, "title", "") or ""))
        if kind is None or ability.ability_type == kind:
            continue
        ability.ability_type = kind
        changed += 1
    return changed
