from ptcgo.game.card_effects.attacks_common import flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _watcheck(ctx):
    """Look at the top 5 of the opponent's deck and put them back in any order."""
    top = ctx.deck_top(5, ctx.opponent_id)
    if len(top) <= 1:
        return
    picked_ids = await ctx.session.prompt_card_chooser(
        ctx.player_id, ctx.source.entity_id, top, len(top), minimum=len(top),
        prompt="Put the cards back in any order.", ordered=True,
    )
    by_id = {c.entity_id: c for c in top}
    order = [by_id[i] for i in picked_ids if i in by_id]
    for card in top:
        if card not in order:
            order.append(card)
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    for card in order:
        deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)


async def _quick_tail_smash_heads(ctx):
    """20 printed plus the 60 the heads rider adds."""
    await ctx.deal_damage(80)


card = PokemonCardDef(
    guid="0876a883-621b-5d93-9a46-78b966ce3264",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1", "Watchog"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Watcheck",
            game_text="Look at the top 5 cards of your opponent's deck and put them back on top of his or her deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_watcheck,
        ),
        Attack(
            title="Quick Tail Smash",
            game_text="Before doing damage, you may flip a coin. If heads, this attack does 60 more damage. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_or_nothing(coins=1, then=_quick_tail_smash_heads),
        ),
    ],
)