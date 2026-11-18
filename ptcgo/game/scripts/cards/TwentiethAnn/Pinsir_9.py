from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="22b2fca0-2f14-522c-a797-6652617d4056",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="TwentiethAnn",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Overhead Throw",
            game_text="This attack does 20 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Heavy Suplex",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)