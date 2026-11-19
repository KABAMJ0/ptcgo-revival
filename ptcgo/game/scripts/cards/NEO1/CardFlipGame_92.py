from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    is_energy_card, is_pokemon_card, is_trainer_card,
)


async def _card_flip_game(ctx):
    prizes = ctx.face_down_prize_cards(ctx.opponent_id)
    if not prizes:
        return
    picks = await ctx.choose_cards(
        prizes, 1, minimum=1,
        prompt="Choose a face-down Prize card to guess")
    if not picks:
        return
    prize = picks[0]
    guess = await ctx.choose(
        "Guess whether that Prize card is an Energy, Trainer, or Pok\u00e9mon card",
        ["Energy card", "Trainer card", "Pok\u00e9mon card"])
    if guess is None:
        return
    await ctx.turn_prize_cards_face_up(cards=[prize],
                                       player_id=ctx.opponent_id)
    correct = (
        (guess == 0 and is_energy_card(prize))
        or (guess == 1 and is_trainer_card(prize))
        or (guess == 2 and is_pokemon_card(prize))
    )
    if correct:
        await ctx.draw_cards(2)


card = ItemCardDef(
    guid="c32d115b-99f9-5088-b666-b13c677efff8",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CardFlipGame.Name",
    display_name="Card-Flip Game",
    searchable_by=["Card-Flip Game"],
    subtypes=[],
    collector_number=92,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=_card_flip_game
)
