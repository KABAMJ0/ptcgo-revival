from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities, AttrID, PokemonTypes
from ptcgo.game.session.passives import Passive


class DimensionValleyPassive(Passive):
    """Each Psychic Pokemon's attacks (both sides) cost 1 Colorless less."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if PokemonTypes.PSYCHIC.value not in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - 1
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


card = StadiumCardDef(
    guid="915776f2-92b4-53ab-97ad-bcf2d4ce25a9",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DimensionValley.Name",
    display_name="Dimension Valley",
    searchable_by=["Dimension Valley", "Stadium"],
    subtypes=["Stadium"],
    collector_number=93,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=DimensionValleyPassive()
)
