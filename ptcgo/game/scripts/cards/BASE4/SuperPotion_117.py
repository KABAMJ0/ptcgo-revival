from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_own_energy_heal

card = ItemCardDef(
    guid="f7d475d4-7947-5aa8-b375-59f37a015e42",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion"],
    subtypes=[],
    collector_number=117,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=discard_own_energy_heal(4),
)
