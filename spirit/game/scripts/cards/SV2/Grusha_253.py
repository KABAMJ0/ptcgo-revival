from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_until_unless_energy

card = SupporterCardDef(
    guid="25123367-5859-5725-a1af-9d86d8765222",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grusha.Name",
    display_name="Grusha",
    searchable_by=["Grusha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=253,
    set_code="SV2",
    rarity=Rarities.Rare,
    effect=draw_until_unless_energy(5, 7)
)
