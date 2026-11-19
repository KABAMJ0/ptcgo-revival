from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations
from ptcgo.game.card_effects.support_common import entity_name


def _unown_on_bench(board, player_id, letters):
    bench = board.find_player_area(player_id, "bench")
    names = {entity_name(card) for card in (bench.children if bench else [])}
    return all(f"Unown [{letter}]" in names for letter in letters)


def _help_condition(board, player_id, pokemon):
    return _unown_on_bench(board, player_id, "HELP")


async def _help(ctx):
    count = len(ctx.hand())
    await ctx.shuffle_into_deck(ctx.hand(), ctx.player_id)
    await ctx.draw_cards(count)


card = PokemonCardDef(
    guid="2eac478a-b120-5d42-aafd-7f3374d21918",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownH.Name",
    display_name="Unown [H]",
    searchable_by=["Unown [H]", "Basic", "UnownH"],
    subtypes=["Basic"],
    collector_number=28,
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
            title="[Help]",
            condition=_help_condition,
            activation=Activations.ONCE_PER_TURN,
            game_text="Once during your turn (before your attack), if you have Unown [H], Unown [E], Unown [L], and Unown [P] on your Bench, you may shuffle your hand into your deck, then draw a new hand of the same number of cards.",
            effect=_help,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)