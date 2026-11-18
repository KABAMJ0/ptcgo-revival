from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_to_bottom_draw

card = SupporterCardDef(
    guid="c947d349-af8d-5f9e-82f4-31d697ad07aa",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kofu.Name",
    display_name="Kofu",
    searchable_by=["Kofu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=165,
    set_code="SV7",
    rarity=Rarities.Rare,
    effect=hand_to_bottom_draw(2, 4)
)
