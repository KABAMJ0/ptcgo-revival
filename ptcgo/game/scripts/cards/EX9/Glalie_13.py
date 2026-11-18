from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae1634d9-6607-5758-822b-e2155becffaf",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name",
    display_name="Glalie",
    searchable_by=["Glalie", "Stage 1", "Glalie"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    abilities=[
        Attack(
            title="Hailstone",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Super Slash",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)