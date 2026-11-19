from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import is_trainer_card

async def _poke_gear(ctx):
    top = ctx.deck_top(7)
    trainers = [card for card in top if is_trainer_card(card)]
    picks = await ctx.choose_cards(
        trainers, 1, minimum=0,
        prompt="Choose a Trainer card to put into your hand",
        display_cards=top)
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()
    ctx.lock_plays(ctx.player_id, is_trainer_card,
                   ctx.session.turn_state.turn_number)


card = ItemCardDef(
    guid="5bb6a32e-1e6e-5218-ac5d-0979cf370797",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokGear.Name",
    display_name="PokéGear",
    searchable_by=["Pok\u00e9Gear"],
    subtypes=[],
    collector_number=88,
    set_code="NEO1",
    rarity=Rarities.Rare,
    effect=_poke_gear
)
