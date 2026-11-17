from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import all_of, draw_until_unless, is_pokemon_card, owned_by

card = SupporterCardDef(
    guid="acc9eb19-26eb-5c64-a744-34c8b3cb3607",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsAriana.Name",
    display_name="Team Rocket's Ariana",
    searchable_by=["Team Rocket's Ariana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=draw_until_unless(5, 8, all_of(is_pokemon_card, owned_by("team rocket")))
)
