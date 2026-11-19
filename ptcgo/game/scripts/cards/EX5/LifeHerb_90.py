from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import excluding, flip_heal_cure, is_pokemon_ex

card = ItemCardDef(
    guid="daa3103a-db7f-5247-81c6-da2c40e1b582",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    effect=flip_heal_cure(excluding(is_pokemon_ex), 60),
)
