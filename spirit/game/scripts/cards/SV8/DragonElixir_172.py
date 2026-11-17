from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="50d65389-5855-5217-aac8-4262900c4aeb",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragonElixir.Name",
    display_name="Dragon Elixir",
    searchable_by=["Dragon Elixir", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
