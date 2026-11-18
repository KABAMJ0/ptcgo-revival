from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="27abd9ef-ad53-5355-9b32-403fd9c00f4c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ForretressG.Name",
    display_name="Forretress G",
    searchable_by=["Forretress G", "Basic", "SP", "ForretressG"],
    subtypes=["Basic", "SP"],
    collector_number=61,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=205,
    abilities=[
        Attack(
            title="Shell Scatter",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Forretress G can't use Shell Scatter during your next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bomb Risk",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Flip a coin. If tails, Forretress G does 80 damage to itself.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)