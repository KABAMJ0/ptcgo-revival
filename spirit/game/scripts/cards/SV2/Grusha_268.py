from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_until_unless_energy

card = SupporterCardDef(
    guid="8e359447-6592-5ad0-bb1d-8066bf7f85e3",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grusha.Name",
    display_name="Grusha",
    searchable_by=["Grusha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=268,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=draw_until_unless_energy(5, 7)
)
