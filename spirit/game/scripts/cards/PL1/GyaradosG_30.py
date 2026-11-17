from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="646849de-7d1b-52c1-af55-7c929ee5b3a3",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GyaradosG.Name",
    display_name="Gyarados G",
    searchable_by=["Gyarados G", "Basic", "SP", "GyaradosG"],
    subtypes=["Basic", "SP"],
    collector_number=30,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=130,
    abilities=[
        Attack(
            title="Wriggle",
            game_text="Flip a coin for each of your opponent's Pok\u00e9mon. If that coin flip is heads, this attack does 30 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Dwindling Wave",
            game_text="Does 100 damage minus 10 damage for each damage counter on Gyarados G.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)