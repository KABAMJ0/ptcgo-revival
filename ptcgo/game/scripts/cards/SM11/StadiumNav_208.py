from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_per_head, is_stadium_card

card = ItemCardDef(
    guid="154d1a24-64b1-55eb-bddb-17570ccfe640",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StadiumNav.Name",
    display_name="Stadium Nav",
    searchable_by=["Stadium Nav", "Item"],
    subtypes=["Item"],
    collector_number=208,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=flip_search_per_head(2, is_stadium_card, 1)
)
