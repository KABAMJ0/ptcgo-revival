from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_energy_card, with_discard_cost


async def holon_lass_look(ctx):
    """Look at as many cards as there are Prize cards left on both sides, take
    any number of Energy cards from them, then shuffle."""
    remaining = sum(
        len(area.children)
        for area in (ctx.board.find_player_area(player_id, "prizePile")
                     for player_id in ctx.board.player_ids)
        if area is not None
    )
    top = ctx.deck_top(remaining) if remaining else []
    if not top:
        return
    energies = [card for card in top if is_energy_card(card)]
    if energies:
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt="Choose any number of Energy cards",
            display_cards=top)
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def _has_card_to_spare(board, player_id):
    """"Discard a card from your hand. If you can't, you can't play this
    card": the hand must hold one card besides this one."""
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and len(hand.children) > 1


card = SupporterCardDef(
    guid="4b2c9f25-2b86-5a72-9d24-1db56be28bc5",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonLass.Name",
    display_name="Holon Lass",
    searchable_by=["Holon Lass", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    condition=_has_card_to_spare,
    effect=with_discard_cost(1, holon_lass_look)
)
