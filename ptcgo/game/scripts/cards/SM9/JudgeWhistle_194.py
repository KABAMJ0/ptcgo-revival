from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.trainers import choose_one, draw_n, named_exactly

card = ItemCardDef(
    guid="86f89d7a-66b7-5155-bf49-5f7aa8fe4274",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name",
    display_name="Judge Whistle",
    searchable_by=["Judge Whistle", "Item"],
    subtypes=["Item"],
    collector_number=194,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=choose_one([("Draw a card", draw_n(1)), ("Put a Judge card from your discard pile into your hand", recover_from_discard(named_exactly("Judge"), count=1, to="hand"))])
)
