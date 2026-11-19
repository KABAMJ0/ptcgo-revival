from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import entity_name, search_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _unown_on_bench(board, player_id, letters):
    bench = board.find_player_area(player_id, "bench")
    names = {entity_name(card) for card in (bench.children if bench else [])}
    return all(f"Unown [{letter}]" in names for letter in letters)


def _give_condition(board, player_id, pokemon):
    return _unown_on_bench(board, player_id, "GIVE")


card = PokemonCardDef(
    guid="ff13f30a-b67b-5e1e-b73f-0117615c86cf",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownG.Name",
    display_name="Unown [G]",
    searchable_by=["Unown [G]", "Basic", "UnownG"],
    subtypes=["Basic"],
    collector_number=27,
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
            title="[Give]",
            condition=_give_condition,
            activation=Activations.ONCE_PER_TURN,
            game_text="Once during your turn (before your attack), if you have Unown [G], Unown [I], Unown [V], and Unown [E] on your Bench, you may flip a coin. If heads, search your deck for a basic Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            effect=flip_gate(then=search_attach_energy(predicate=is_basic_energy_card, count=1)),
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)