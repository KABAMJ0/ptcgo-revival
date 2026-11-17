from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="464389c9-1151-5e51-b255-07036b36be79",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RampardosGL.Name",
    display_name="Rampardos GL",
    searchable_by=["Rampardos GL", "Basic", "SP", "RampardosGL"],
    subtypes=["Basic", "SP"],
    collector_number=11,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=409,
    abilities=[
        Attack(
            title="Trample",
            game_text="Flip a coin for each Benched Pok\u00e9mon (both yours and your opponent's). If that coin flip is heads, this attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rend",
            game_text="If the Defending Pok\u00e9mon has any damage counters on it, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)