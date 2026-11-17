from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import basic_energy_of

card = SupporterCardDef(
    guid="4ea788ee-a424-53d9-99c6-b7709a2b0fa4",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clemont.Name",
    display_name="Clemont",
    searchable_by=["Clemont", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(basic_energy_of("lightning"), count=4)
)
