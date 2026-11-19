from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import unafflicted


def _look_at_top_condition(board, player_id, pokemon) -> bool:
    return unafflicted(board, player_id, pokemon)


async def _look_at_top_and_shuffle(ctx):
    results = await ctx.flip_coins(1, "Cunning")
    if not (results and results[0]):
        return
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    await ctx.reveal_cards(top, to_player=ctx.player_id)
    if await ctx.ask_yes_no("Have your opponent shuffle his or her deck?"):
        await ctx.shuffle_deck(ctx.opponent_id)


async def _mind_shock(ctx):
    """Mind Shock: no Weakness or Resistance on this hit."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True,
                          apply_modifiers=False)

card = PokemonCardDef(
    guid="4eccbf9b-71fb-568c-85d8-d2bb0cdd9f52",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkSlowking.Name",
    display_name="Dark Slowking",
    searchable_by=["Dark Slowking", "Stage 1", "DarkSlowking"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=199,
    abilities=[
        Ability(
            title="Cunning",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, look at the top card of your opponent's deck. Then, you may have your opponent shuffle his or her deck. This power can't be used if Dark Slowking is Asleep, Confused, or Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            condition=_look_at_top_condition,
            effect=_look_at_top_and_shuffle,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness or Resistance for this attack.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=_mind_shock,
        ),
    ],
)