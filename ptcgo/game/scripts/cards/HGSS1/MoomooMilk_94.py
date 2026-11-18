from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_heal_chosen

card = ItemCardDef(
    guid="7c4974db-2ae3-5fff-a125-f35ca250271b",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoomooMilk.Name",
    display_name="Moomoo Milk",
    searchable_by=["Moomoo Milk", "Item"],
    subtypes=["Item"],
    collector_number=94,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=flip_heal_chosen(3, 2)
)
