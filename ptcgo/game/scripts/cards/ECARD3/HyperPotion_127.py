from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import heal_by_discarded_energy

card = ItemCardDef(
    guid="c00ae5c6-5949-5fd6-ae78-31766395596a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HyperPotion.Name",
    display_name="Hyper Potion",
    searchable_by=["Hyper Potion"],
    subtypes=[],
    collector_number=127,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=heal_by_discarded_energy(3, 5)
)
