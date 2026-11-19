from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.attacks_common import count_energy, flip_damage
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.card_effects.passives_common import unafflicted


def _is_metal_energy(card):
    return energy_provides_type(card, PokemonTypes.METAL.value)


def _to_heatran(pokemon, ctx):
    return pokemon is ctx.source


def _smelt_condition(board, player_id, pokemon):
    return unafflicted(board, player_id, pokemon)         and can_move_energy(_is_metal_energy)(board, player_id, pokemon)


card = PokemonCardDef(
    guid="ab58a6bf-8261-5d01-8bcd-67eeeb760fbc",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic", "Heatran"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Ability(
            title="Smelt",
            condition=_smelt_condition,
            activation=Activations.ONCE_PER_TURN,
            game_text="Once during your turn (before your attack), you may move a Metal Energy attached to 1 of your Pok\u00e9mon to Heatran. This power can't be used if Heatran is affected by a Special Condition.",
            effect=move_energy_between(predicate=_is_metal_energy, count=1, to_pred=_to_heatran),
        ),
        Attack(
            title="Heavy Metal",
            game_text="Flip a coin for each Metal Energy attached to Heatran. This attack does 40 damage plus 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=flip_damage(per_heads=20, base=40, coins_from=count_energy("self", PokemonTypes.METAL, cards=True)),
        ),
    ],
)