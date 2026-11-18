from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, draw_until_unless, is_pokemon_card, owned_by

card = SupporterCardDef(
    guid="4b5a9d80-e5ae-53ea-ad15-1c9cbe6dbc45",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsAriana.Name",
    display_name="Team Rocket's Ariana",
    searchable_by=["Team Rocket's Ariana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=224,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=draw_until_unless(5, 8, all_of(is_pokemon_card, owned_by("team rocket")))
)
