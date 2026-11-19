from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw

def first_turn(board, player_id, pokemon):
    turn_state = getattr(board, "turn_state", None)
    return turn_state is not None and turn_state.turn_number <= 2
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="1b38908f-db0c-5719-b8f6-9d305fb45330",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabillyex.Name",
    display_name="Squawkabilly ex",
    searchable_by=["Squawkabilly ex", "Basic", "ex", "Squawkabillyex"],
    subtypes=["Basic", "ex"],
    collector_number=169,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=931,
    abilities=[
        Ability(
            title="Squawk and Seize",
            game_text="Once during your first turn, you may discard your hand and draw 6 cards. You can't use more than 1 Squawk and Seize Ability during your turn.",
            activation=Activations.ONCE_PER_TURN,
            condition=first_turn,
            shared_once_per_turn="Squawk and Seize",
            effect=discard_then_draw(0, 6, whole_hand=True),
        ),
        Attack(
            title="Motivate",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=attach_from_discard(predicate=is_basic_energy_card, count=2, minimum=0, target=lambda p: not is_in_active_spot(p), prompt='Choose up to 2 basic Energy cards to attach'),
        ),
    ],
)