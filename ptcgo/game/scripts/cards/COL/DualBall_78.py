from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_basic_count

card = ItemCardDef(
    guid="60c86cf1-1828-572d-b02c-0216da6e471b",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=flip_search_basic_count(2, avoid_baby=False)
)
