from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard
from spirit.game.card_effects.trainers import choose_one, draw_n, named_exactly

card = ItemCardDef(
    guid="ad58126a-a0ae-58e9-a4ec-db600586365d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name",
    display_name="Judge Whistle",
    searchable_by=["Judge Whistle", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=choose_one([("Draw a card", draw_n(1)), ("Put a Judge card from your discard pile into your hand", recover_from_discard(named_exactly("Judge"), count=1, to="hand"))])
)
