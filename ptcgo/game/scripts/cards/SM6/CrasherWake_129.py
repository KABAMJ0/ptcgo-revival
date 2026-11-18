from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of, discard_typed_then_search

card = SupporterCardDef(
    guid="807f8cdd-a4a5-5433-b4e7-063c48cb3744",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrasherWake.Name",
    display_name="Crasher Wake",
    searchable_by=["Crasher Wake", "Supporter"],
    subtypes=["Supporter"],
    collector_number=129,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    effect=discard_typed_then_search(2, basic_energy_of("water"), 2)
)
