from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="02cca661-90b2-52e7-b5c6-5d3cdf8e2a12",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Keldeoex.Name",
    display_name="Keldeo ex",
    searchable_by=["Keldeo ex", "Basic", "ex", "Keldeoex"],
    subtypes=["Basic", "ex"],
    collector_number=167,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=647,
    abilities=[
        Attack(
            title="Gale Thrust",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack does 90 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)