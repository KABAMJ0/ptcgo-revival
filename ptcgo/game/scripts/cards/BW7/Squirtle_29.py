from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.session.passives import carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_bonus

def _shell_shield(calc, carrier):
    """All damage to this Pokemon while it sits on the Bench."""
    holder = carrier_pokemon(carrier)
    return (holder is not None and calc.target is holder
            and not calc.to_active and calc.is_attack)


card = PokemonCardDef(
    guid="6d9a9ccf-b043-56d2-86d3-8dff78e6c9cb",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=7,
    abilities=[
        Ability(
            title="Shell Shield",
            game_text="As along as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            passive=prevent_damage_when(_shell_shield, any_side=True),
        ),
        Attack(
            title="Water Splash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)