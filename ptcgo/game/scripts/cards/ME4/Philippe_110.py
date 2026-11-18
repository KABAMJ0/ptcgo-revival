from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of

card = SupporterCardDef(
    guid="ed536b51-5b65-53b5-adf3-0ef37a6b83df",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Philippe.Name",
    display_name="Philippe",
    searchable_by=["Philippe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="ME4",
    rarity=Rarities.Rare,
    effect=attach_from_discard(basic_energy_of("metal"), count=2, target="choice")
)
