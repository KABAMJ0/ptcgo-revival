from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f03c86d8-ebd4-597d-bab5-8d7c986c2a68",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RaichuGL.Name",
    display_name="Raichu GL",
    searchable_by=["Raichu GL", "Basic", "SP", "RaichuGL"],
    subtypes=["Basic", "SP"],
    collector_number=31,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=26,
    abilities=[
        Attack(
            title="Thunder Throw",
            game_text="Choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Repeat Lightning",
            game_text="Does 30 damage plus 10 more damage for each of your opponent's Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)