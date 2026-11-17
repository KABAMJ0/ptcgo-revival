from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96205353-7ba1-5177-8749-9edede61f8f2",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    display_name="Zigzagoon",
    searchable_by=["Zigzagoon", "Basic", "Zigzagoon"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="TK1B",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=263,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)