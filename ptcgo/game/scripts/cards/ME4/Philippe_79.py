from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of

card = SupporterCardDef(
    guid="57f2936a-751b-5173-9e7c-962bae1a441f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Philippe.Name",
    display_name="Philippe",
    searchable_by=["Philippe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    effect=attach_from_discard(basic_energy_of("metal"), count=2, target="choice")
)
