from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_reorder

card = ItemCardDef(
    guid="32acf046-cf2f-527e-9d42-a512df600cee",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokdex.Name",
    display_name="Pokédex",
    searchable_by=["Pok\u00e9dex"],
    subtypes=[],
    collector_number=87,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=look_top_reorder(5)
)
