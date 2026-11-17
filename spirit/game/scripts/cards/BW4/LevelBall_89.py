from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import all_of, is_pokemon_card, pokemon_with_hp_at_most

card = ItemCardDef(
    guid="57ab581f-a00e-56c7-a5b4-a6372eab281e",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LevelBall.Name",
    display_name="Level Ball",
    searchable_by=["Level Ball", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(all_of(is_pokemon_card, pokemon_with_hp_at_most(90)), count=1)
)
