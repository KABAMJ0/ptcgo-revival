from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cddc897c-1758-5f21-8c4c-26dd71224a7b",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dodrio.Name",
    display_name="Dodrio",
    searchable_by=["Dodrio", "Stage 1", "Dodrio"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    family_id=84,
    abilities=[
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Triple Pick",
            game_text="Choose 3 of your opponent's Evolved Pok\u00e9mon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)