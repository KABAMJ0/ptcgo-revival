from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations, TrainerCardDef, def_for
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import entity_name, recover_from_discard


def _unown_on_bench(board, player_id, letters):
    bench = board.find_player_area(player_id, "bench")
    names = {entity_name(card) for card in (bench.children if bench else [])}
    return all(f"Unown [{letter}]" in names for letter in letters)


def _want_condition(board, player_id, pokemon):
    return _unown_on_bench(board, player_id, "WANT")


def _is_trainer_card(card):
    return isinstance(def_for(card.archetype_id), TrainerCardDef)


card = PokemonCardDef(
    guid="2fac3520-9426-56a0-bdcd-73b73d2077bc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownW.Name",
    display_name="Unown [W]",
    searchable_by=["Unown [W]", "Basic", "UnownW"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Want]",
            condition=_want_condition,
            activation=Activations.ONCE_PER_TURN,
            game_text="Once during your turn (before your attack), if you have Unown [W], Unown [A], Unown [N], and Unown [T] on your Bench, you may flip a coin. If heads, put a Trainer card from your discard pile into your hand.",
            effect=flip_gate(then=recover_from_discard(predicate=_is_trainer_card, count=1, minimum=0)),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)