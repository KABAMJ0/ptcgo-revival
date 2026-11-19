from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holon_fossil

card = ItemCardDef(
    guid="1a2d4b1c-8a4d-579a-971b-501df98c89dd",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonFossil.Name",
    display_name="Holon Fossil",
    searchable_by=["Holon Fossil", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=holon_fossil()
)
