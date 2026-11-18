from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a9662f29-867a-5252-b914-e4c738f8849b",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SkarmoryEX.Name",
    display_name="Skarmory-EX",
    searchable_by=["Skarmory-EX", "Basic", "EX", "SkarmoryEX"],
    subtypes=["Basic", "EX"],
    collector_number=145,
    set_code="XY1",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=227,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Tailspin Piledriver",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 40 more damage.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)