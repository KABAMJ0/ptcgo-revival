from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, excluding, flip_heal_cure, is_pokemon_card, is_pokemon_ex

card = ItemCardDef(
    guid="25f92163-6207-523b-83fc-4811270e30b4",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=flip_heal_cure(all_of(is_pokemon_card, excluding(is_pokemon_ex)), 60, 1)
)
