from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_n

card = SupporterCardDef(
    guid="4998942b-1b73-5f08-8bc4-779c04c31b3d",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name",
    display_name="Tierno",
    searchable_by=["Tierno", "Supporter"],
    subtypes=["Supporter"],
    collector_number=112,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=draw_n(3)
)
