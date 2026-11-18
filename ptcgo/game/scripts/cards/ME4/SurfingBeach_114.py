from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of, stadium_ability, switch_typed_active

card = StadiumCardDef(
    guid="a44610ff-5ee6-5a4a-a45e-b60b6d6b2b94",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurfingBeach.Name",
    display_name="Surfing Beach",
    searchable_by=["Surfing Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="ME4",
    rarity=Rarities.Rare,
    ability=stadium_ability('Surfing Beach', switch_typed_active(pokemon_of("water")))
)
