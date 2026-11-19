from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import TakesLessPassive

def _printed_name(pokemon) -> str:
    definition = def_for(getattr(pokemon, "archetype_id", None))
    printed = getattr(definition, "display_name", "") or ""
    return "".join(ch for ch in printed.lower() if ch.isalnum())


class _OnixShield(TakesLessPassive):
    """Onix-GX, on either side, takes 40 less from attacks after Weakness and
    Resistance."""

    def __init__(self):
        super().__init__(40, protects=lambda target, carrier: _printed_name(target) == "onixgx")

card = StadiumCardDef(
    guid="f9b480aa-f3b2-5e27-95aa-b816005f0e33",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksPewterCityGym.Name",
    display_name="Brock's Pewter City Gym",
    searchable_by=["Brock's Pewter City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=54,
    set_code="HF",
    rarity=Rarities.Uncommon,
    passive=_OnixShield(),
)
