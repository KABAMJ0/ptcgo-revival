from ptcgo.game.card_effects.attacks_common import discard_random_from_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import effective_bench_capacity


def _shedinja(card) -> bool:
    return getattr(def_for(getattr(card, "archetype_id", "") or ""),
                   "display_name", "") == "Shedinja"


async def _cast_off_shell(ctx):
    bench = ctx.session.board_state.find_player_area(ctx.player_id, "bench")
    if bench is None or len(bench.children) >= effective_bench_capacity(
            ctx.session.board_state, ctx.player_id):
        return
    candidates = [card for card in list(ctx.hand()) + list(ctx.discard_pile())
                  if _shedinja(card)]
    if not candidates:
        return
    if not await ctx.ask_yes_no("Put Shedinja onto your Bench as a Basic Pokémon?"):
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose Shedinja from your hand or discard pile")
    for card in picks:
        await ctx.bench_pokemon(card)


async def _chip_off(ctx):
    await ctx.deal_damage()
    excess = ctx.hand_size(ctx.opponent_id) - 5
    if ctx.hand_size(ctx.opponent_id) >= 6 and excess > 0:
        await discard_random_from_hand(ctx, ctx.opponent_id, excess)

card = PokemonCardDef(
    guid="80f62e61-eaab-5f4c-897d-15bb9e64f5e6",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Cast-off Shell",
            game_text="Once during your turn, when you play Ninjask from your hand to evolve 1 of your Pok\u00e9mon and if your Bench isn't full, you may put Shedinja onto your Bench as a Basic Pok\u00e9mon from your hand or your discard pile.",
            trigger=Triggers.ON_EVOLVE,
            effect=_cast_off_shell,
        ),
        Attack(
            title="Chip Off",
            game_text="If your opponent has 6 or more cards in his or her hand, discard a number of cards without looking until your opponent has 5 cards left in his or her hand.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=_chip_off,
        ),
    ],
)