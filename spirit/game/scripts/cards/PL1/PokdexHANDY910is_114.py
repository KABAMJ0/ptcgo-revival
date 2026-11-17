from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import look_at_top

card = ItemCardDef(
    guid="e0650df2-4de9-5e70-89c2-7ab10d9de41b",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokdexHANDY910is.Name",
    display_name="Pokédex HANDY910is",
    searchable_by=["Pok\u00e9dex HANDY910is", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=look_at_top(2, take=1, rest="bottom", minimum=0)
)
