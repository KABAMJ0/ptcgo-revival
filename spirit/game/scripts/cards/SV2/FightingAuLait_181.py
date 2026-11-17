from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_item
from spirit.game.card_effects.trainers import behind_on_prizes

card = ItemCardDef(
    guid="1699f16d-7256-5025-bee2-eff52776d239",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingAuLait.Name",
    display_name="Fighting Au Lait",
    searchable_by=["Fighting Au Lait", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=heal_item(amount=60, scope="choice"), condition=behind_on_prizes()
)
