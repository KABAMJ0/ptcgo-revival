from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.card_effects.passives_common import attack_cost_modifier, pokemon_of_types
from ptcgo.game.attributes import Rarities, PokemonTypes

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
    passive=attack_cost_modifier(-1, pred=pokemon_of_types(PokemonTypes.PSYCHIC.value))
)
