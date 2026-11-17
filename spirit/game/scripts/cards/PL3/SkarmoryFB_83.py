from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f08a11dd-ce79-5081-a253-2151e7a4f300",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SkarmoryFB.Name",
    display_name="Skarmory FB",
    searchable_by=["Skarmory FB", "Basic", "SP", "SkarmoryFB"],
    subtypes=["Basic", "SP"],
    collector_number=83,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Silver Feather",
            game_text="During your opponent's next turn, when your opponent puts a Basic Pok\u00e9mon from his or her hand onto his or her Bench, put 2 damage counters on that Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Metal Max",
            game_text="Discard all Metal Energy attached to Skarmory FB. Flip a coin for each Energy card you discarded. This attack does 20 damage plus 40 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)