from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.models.board import PokemonEntity


async def blaines_quiz2_guess(ctx):
    """Put a card face down; the opponent names its class. Right: they draw 2.
    Wrong: you draw 2. The card returns to hand either way."""
    hand = [card for card in ctx.hand() if card is not ctx.source]
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1, prompt="Choose a card to put face down")
    if not picks:
        return
    card = picks[0]
    if is_energy_card(card):
        actual = 0
    elif isinstance(card, PokemonEntity):
        actual = 2
    else:
        actual = 1
    guess = await ctx.choose(
        "Your opponent put a card face down in front of them. What is it?",
        ["Energy card", "Trainer card", "Pokémon card"],
        player_id=ctx.opponent_id)
    if guess == actual:
        await ctx.draw_cards(2, ctx.opponent_id)
    else:
        await ctx.draw_cards(2)


card = ItemCardDef(
    guid="35a87a27-b12a-5237-bcda-db283205e1a5",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesQuiz2.Name",
    display_name="Blaine's Quiz #2",
    searchable_by=["Blaine's Quiz #2"],
    subtypes=[],
    collector_number=111,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    effect=blaines_quiz2_guess
)
