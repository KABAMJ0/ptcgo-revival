from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import basic_energy_of, discard_typed_then_search

card = SupporterCardDef(
    guid="33528646-2ab5-5dab-91c5-b0f7610b8d5c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrasherWake.Name",
    display_name="Crasher Wake",
    searchable_by=["Crasher Wake", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=discard_typed_then_search(2, basic_energy_of("water"), 2)
)
