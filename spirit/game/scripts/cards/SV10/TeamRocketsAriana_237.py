from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import all_of, draw_until_unless, is_pokemon_card, owned_by

card = SupporterCardDef(
    guid="0efa6703-3054-56d6-a407-42adc41d020b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsAriana.Name",
    display_name="Team Rocket's Ariana",
    searchable_by=["Team Rocket's Ariana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=237,
    set_code="SV10",
    rarity=Rarities.Rare,
    effect=draw_until_unless(5, 8, all_of(is_pokemon_card, owned_by("team rocket")))
)
