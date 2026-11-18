from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import if_heads, is_basic_energy_card

card = ItemCardDef(
    guid="ea8928ab-6e2c-522b-9385-f69a2d3471a3",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySticker.Name",
    display_name="Energy Sticker",
    searchable_by=["Energy Sticker", "Item"],
    subtypes=["Item"],
    collector_number=159,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    effect=if_heads(attach_from_discard(is_basic_energy_card, count=1, target="choice"))
)
