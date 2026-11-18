from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_hand_to_bottom_draw_same

card = ItemCardDef(
    guid="7c99bdd3-7cc1-538d-8ec0-4e1019fc843c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MeddlingMemo.Name",
    display_name="Meddling Memo",
    searchable_by=["Meddling Memo", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=opponent_hand_to_bottom_draw_same()
)
