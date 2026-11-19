from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_choice

from ptcgo.game.attributes import GameSequence
from ptcgo.game.data_utils import Activations


async def trickery(ctx):
    """Switch 1 of your Prizes with the top card of your deck; both stay face
    down."""
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
    guid="edfc7846-65f2-53b4-a48f-ba6ff75e5439",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="BASE5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=19,
    abilities=[
        Ability(
            title="Trickery",
            game_text="Once during your turn (before your attack), you may switch 1 of your Prizes with the top card of your deck. This power can't be used if Rattata is Asleep, Confused, or Paralyzed.",
            activation=Activations.ONCE_PER_TURN,
            effect=trickery,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_choice(heads=20, tails=10),
        ),
    ],
)