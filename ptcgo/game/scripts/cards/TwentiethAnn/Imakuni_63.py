from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import confuse_own_active

card = SupporterCardDef(
    guid="341cc365-8750-5f9e-b179-09265beb7dac",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Imakuni.Name",
    display_name="Imakuni?",
    searchable_by=["Imakuni?", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=confuse_own_active()
)
