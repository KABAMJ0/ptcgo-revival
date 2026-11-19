from ptcgo.game.data_utils import Attack, Ability, PokemonCardDef, Triggers
from ptcgo.game.attributes import GameSequence, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage


async def pantomime(ctx):
    """Switch 1 of your face-down Prize cards with the top card of your deck.

    Both cards stay face down: the Prize card goes on top of the deck under
    WithOpenPrizeCards (no intro, so the fan does not tear down face-up) and the
    deck's top card is moved into the vacated Prize slot, then re-hidden."""
    if not await ctx.ask_yes_no("Switch a Prize card with the top card of your deck?"):
        return
    top = ctx.deck_top(1)
    if not top:
        return
    card = top[0]
    prize_area = ctx.board.find_player_area(ctx.player_id, "prizePile")
    prizes = list(prize_area.children) if prize_area else []
    if not prizes:
        return
    picked_ids = await ctx.session._prompt_prize_pick(
        ctx.player_id, [c.entity_id for c in prizes], 1,
        prompt="Choose a face-down Prize card to switch.",
    )
    picked = ctx.board.get_entity(picked_ids[0]) if picked_ids else None
    if picked is None or picked.parent is not prize_area:
        return
    slot = getattr(picked, "board_slot", None)
    if slot is None:
        slot = prizes.index(picked)
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    both = list(ctx.session.players.values())
    position = len(deck.children)
    if not ctx.board.move_card(picked.entity_id, deck.entity_id):
        return
    move = ctx.session._entity_moved_msg(picked.entity_id, deck.entity_id, position)
    for viewer in both:
        await ctx.session.send_game_sequence(
            [viewer], GameSequence.WITH_OPEN_PRIZE_CARDS, [move])
    if ctx.board.move_card(card.entity_id, prize_area.entity_id, slot):
        await ctx.session.send_game_sequence(
            both, GameSequence.GROUPED_MOVE,
            [ctx.session._entity_moved_msg(card.entity_id, prize_area.entity_id, slot)])
        await ctx.session.send_game_sequence(
            [ctx.session.players[ctx.player_id]], GameSequence.GROUPED_MOVE,
            [ctx.session._attributes_reset_msg(card.entity_id)])

card = PokemonCardDef(
    guid="c4252959-5d3f-54f5-87e0-a1c87270836e",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic", "MrMime"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="GUM",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Ability(
            title="Pantomime",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may switch 1 of your face-down Prize cards with the top card of your deck.",
            trigger=Triggers.ON_PLAY,
            effect=pantomime,
        ),
        Attack(
            title="Juggling",
            game_text="Flip 4 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)