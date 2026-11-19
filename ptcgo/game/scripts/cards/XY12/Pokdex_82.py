from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_reorder

card = ItemCardDef(
    guid="6dea3f2c-dac3-5b88-ab90-b6d0ad542c16",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=look_top_reorder(5)
)
