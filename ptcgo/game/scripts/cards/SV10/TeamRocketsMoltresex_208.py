from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29b6f152-6a66-5841-ac96-62d6738866a0",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMoltresex.Name",
    display_name="Team Rocket's Moltres ex",
    searchable_by=["Team Rocket's Moltres ex", "Basic", "ex", "TeamRocketsMoltresex"],
    subtypes=["Basic", "ex"],
    collector_number=208,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=146,
    abilities=[
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=unimplemented,
        ),
        Attack(
            title="Evil Incineration",
            game_text="Discard a Team Rocket's Energy from this Pok\u00e9mon. If you do, discard your opponent's Active Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)