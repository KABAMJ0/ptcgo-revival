from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = SupporterCardDef(
    guid="6d5db431-792f-569d-a8bb-dbed8aed8a43",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasGuidance.Name",
    display_name="Cynthia's Guidance",
    searchable_by=["Cynthia's Guidance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=136,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    effect=look_at_top(7, take=1, rest="shuffle", minimum=1)
)
