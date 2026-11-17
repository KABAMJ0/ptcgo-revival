from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import all_of, draw_until_unless, is_pokemon_card, named

card = SupporterCardDef(
    guid="c0e00d3c-4c3b-5be2-8e3e-90a33b4f64a1",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsAriana.Name",
    display_name="Team Rocket's Ariana",
    searchable_by=["Team Rocket's Ariana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=202,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    effect=draw_until_unless(5, 8, all_of(is_pokemon_card, named("team rocket")))
)
