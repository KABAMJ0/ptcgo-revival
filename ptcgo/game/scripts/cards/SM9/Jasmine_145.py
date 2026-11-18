from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of, search_going_second

card = SupporterCardDef(
    guid="cde7cd61-daf1-5a13-8cc7-0440b28d8ca5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jasmine.Name",
    display_name="Jasmine",
    searchable_by=["Jasmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=search_going_second(pokemon_of("metal"), 1, 5)
)
