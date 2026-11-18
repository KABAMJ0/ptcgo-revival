from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.card_effects.trainers import pokemon_named
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29f0d13e-6033-5d3b-8eb9-3bf4aeb42407",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grubbin.Name",
    display_name="Grubbin",
    searchable_by=["Grubbin", "Basic", "Grubbin"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=736,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for up to 2 Grubbin and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(pokemon_named("Grubbin"), count=2),
        ),
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
        ),
    ],
)