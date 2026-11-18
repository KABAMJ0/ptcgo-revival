from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_own_energy_heal

card = ItemCardDef(
    guid="aee1a71a-3df8-5067-b0cb-195ae1ab3724",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion"],
    subtypes=[],
    collector_number=90,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=discard_own_energy_heal(4)
)
