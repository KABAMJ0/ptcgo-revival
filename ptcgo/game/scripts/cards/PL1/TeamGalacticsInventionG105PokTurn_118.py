from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype, return_pokemon_to_hand

card = ItemCardDef(
    guid="8991ce01-7205-5d81-8fd1-06ecd341bb96",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamGalacticsInventionG105PokTurn.Name",
    display_name="Team Galactic's Invention G-105 Poké Turn",
    searchable_by=["Team Galactic's Invention G-105 Pok\u00e9 Turn", "Item"],
    subtypes=["Item"],
    collector_number=118,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    effect=return_pokemon_to_hand(predicate=pokemon_of_subtype("SP"))
)
