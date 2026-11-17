from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import all_of, is_pokemon_card, pokemon_with_hp_at_most

card = ItemCardDef(
    guid="543b23c8-9679-5054-a8c6-3f96358f1781",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LevelBall.Name",
    display_name="Level Ball",
    searchable_by=["Level Ball", "Item"],
    subtypes=["Item"],
    collector_number=76,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_pokemon_card, pokemon_with_hp_at_most(90)), count=1)
)
