from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_pokemon, return_pokemon_to_hand

card = SupporterCardDef(
    guid="c6ebe671-3d63-5254-bf2d-eb8998c5e1eb",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Penny.Name",
    display_name="Penny",
    searchable_by=["Penny", "Supporter"],
    subtypes=["Supporter"],
    collector_number=239,
    set_code="SV1",
    rarity=Rarities.Rare,
    effect=return_pokemon_to_hand(predicate=is_basic_pokemon)
)
