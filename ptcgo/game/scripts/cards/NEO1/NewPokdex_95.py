from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import look_top_reorder

card = ItemCardDef(
    guid="a6380331-b72d-51d8-9539-ff06e088b34a",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NewPokdex.Name",
    display_name="New Pokédex",
    searchable_by=["New Pok\u00e9dex"],
    subtypes=[],
    collector_number=95,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    effect=look_top_reorder(5)
)
