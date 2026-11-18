from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_per_head, is_basic_pokemon

card = ItemCardDef(
    guid="a4ae3295-5f22-5d38-b7ed-7319d47bb764",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=72,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    effect=flip_search_per_head(2, is_basic_pokemon, 1)
)
