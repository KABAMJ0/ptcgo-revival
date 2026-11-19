from ptcgo.game.data_utils import StadiumCardDef, def_for
from ptcgo.game.attributes import PokemonTypes, Rarities
from ptcgo.game.session.passives import Passive, is_basic_energy


def _is_delta(pokemon) -> bool:
    """A Pokemon with the printed delta marker ("Beedrill δ")."""
    definition = def_for(pokemon.archetype_id)
    return "\u03b4" in (getattr(definition, "display_name", "") or "")


class HolonResearchTowerPassive(Passive):
    """Basic Energy attached to a delta Pokemon provides its usual type and
    Metal, still one unit at a time."""

    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or not is_basic_energy(energy) or not _is_delta(holder):
            return options
        metal = PokemonTypes.METAL.value
        types = {type_value for option in options for type_value in option}
        types.add(metal)
        return [[type_value] for type_value in sorted(types)]


card = StadiumCardDef(
    guid="d19f95b5-ca44-52b3-8d3a-6fd82c1568ff",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonResearchTower.Name",
    display_name="Holon Research Tower",
    searchable_by=["Holon Research Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    passive=HolonResearchTowerPassive(),
)
