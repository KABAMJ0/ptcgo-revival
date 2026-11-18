from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8457d88e-f8f1-512c-9c60-2d0ad54767cc",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmoryex.Name",
    display_name="Skarmory ex",
    searchable_by=["Skarmory ex", "Basic", "ex", "Skarmoryex"],
    subtypes=["Basic", "ex"],
    collector_number=98,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=227,
    abilities=[
        Ability(
            title="Metal Gravity",
            game_text="If your opponent's Active Pok\u00e9mon retreats and has 40 or more remaining HP, put 3 damage counters on that Pok\u00e9mon. You can't use more than 1 Metal Gravity Pok\u00e9-Body each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)