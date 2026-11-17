from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_at_top

card = ItemCardDef(
    guid="5d41809b-f503-5ebc-a5db-8d07eb58bfea",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokdexHANDY910is.Name",
    display_name="Pokédex HANDY910is",
    searchable_by=["Pok\u00e9dex HANDY910is", "Item"],
    subtypes=["Item"],
    collector_number=111,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    effect=look_at_top(2, take=1, rest="bottom", minimum=0)
)
