from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="364cbc74-eb1b-5d1f-bf0c-f8eeb1995425",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GastrodonWestSea.Name",
    display_name="Gastrodon West Sea",
    searchable_by=["Gastrodon West Sea", "Stage 1", "GastrodonWestSea"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosWestSea.Name",
    family_id=422,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
        Attack(
            title="Muddy Bomb",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 30 damage to that Pok\u00e9mon and 10 damage to each of your opponent's other Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Raging Sea",
            game_text="Does 60 damage plus 10 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)