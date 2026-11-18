from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of, stadium_ability, switch_typed_active

card = StadiumCardDef(
    guid="8ab8254b-5e01-51e5-83a7-737d9bb93f66",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SurfingBeach.Name",
    display_name="Surfing Beach",
    searchable_by=["Surfing Beach", "Stadium"],
    subtypes=["Stadium"],
    collector_number=129,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    ability=stadium_ability('Surfing Beach', switch_typed_active(pokemon_of("water")))
)
