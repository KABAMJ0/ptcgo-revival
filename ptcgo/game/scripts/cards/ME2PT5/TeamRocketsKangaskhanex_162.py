from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b26593f5-bc6f-51ed-b5f1-50d5a5416da2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKangaskhanex.Name",
    display_name="Team Rocket's Kangaskhan ex",
    searchable_by=["Team Rocket's Kangaskhan ex", "Basic", "ex", "TeamRocketsKangaskhanex"],
    subtypes=["Basic", "ex"],
    collector_number=162,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Attack(
            title="Comet Punch",
            game_text="Flip 4 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Wicked Impact",
            game_text="If you played a Supporter card that has \"Team Rocket\" in its name from your hand during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)