from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4f2dac9d-c7b2-5a5a-8e58-044e9b53ce8c",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ElectrodeG.Name",
    display_name="Electrode G",
    searchable_by=["Electrode G", "Basic", "SP", "ElectrodeG"],
    subtypes=["Basic", "SP"],
    collector_number=39,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=101,
    abilities=[
        Attack(
            title="Reckless Bomb",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Electrode G does 100 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Reflect Energy",
            game_text="Move an Energy card attached to Electrode G to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)