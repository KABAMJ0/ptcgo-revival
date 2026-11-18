from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="597bbfbb-e404-54f3-8ec7-4046121adb05",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Grip and Squeeze",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Power Guillotine",
            game_text="Flip 2 coins. If either of them is tails, this attack's base damage is 10 instead of 100.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)