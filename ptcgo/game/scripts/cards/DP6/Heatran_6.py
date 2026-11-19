from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.session.passives import is_basic_energy
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.card_effects.passives_common import unafflicted


def _is_fire_energy(card):
    return energy_provides_type(card, PokemonTypes.FIRE.value)


def _to_heatran(pokemon, ctx):
    return pokemon is ctx.source


def _flash_fire_condition(board, player_id, pokemon):
    return unafflicted(board, player_id, pokemon)         and can_move_energy(_is_fire_energy)(board, player_id, pokemon)


card = PokemonCardDef(
    guid="4b4c00b5-4d8b-5afc-a450-a4ef7501e1fd",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name",
    display_name="Heatran",
    searchable_by=["Heatran", "Basic", "Heatran"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Ability(
            title="Flash Fire",
            condition=_flash_fire_condition,
            activation=Activations.ONCE_PER_TURN,
            game_text="Once during your turn (before your attack), you may move a Fire Energy attached to 1 of your Pok\u00e9mon to Heatran. This power can't be used if Heatran is affected by a Special Condition.",
            effect=move_energy_between(predicate=_is_fire_energy, count=1, to_pred=_to_heatran),
        ),
        Attack(
            title="Magma Storm",
            game_text="You may discard as many basic Energy cards as you like attached to Heatran. If you do, this attack does 40 damage plus 20 more damage for each Energy card you discarded.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=discard_for_bonus(source="self-energy", predicate=is_basic_energy, max_count=99, per=20, base=40, prompt="Choose any number of basic Energy cards to discard"),
        ),
    ],
)