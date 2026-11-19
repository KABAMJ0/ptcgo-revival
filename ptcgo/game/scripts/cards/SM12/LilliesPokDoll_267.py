from ptcgo.game.data_utils import FossilItemCardDef, Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import FossilBodyPassive
from ptcgo.game.session.effects import full_stack


async def _doll_to_bottom(ctx):
    doll = ctx.source
    was_active = doll is ctx.my_active()
    discard = ctx.board.find_player_area(ctx.player_id, "discard")
    if discard is not None and discard.entity_id not in ctx.visual_targets:
        ctx.visual_targets.append(discard.entity_id)
    await ctx.discard_cards([card for card in full_stack(doll) if card is not doll])
    await ctx.put_on_bottom_of_deck(doll)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pok\u00e9mon left")
        ctx.deferred_actions.append(_promote)


def _doll_ability():
    return Ability(
        "Discard",
        "At any time during your turn, you may discard all cards from this "
        "Pok\u00e9mon and put it on the bottom of your deck.",
        activation=Activations.ONCE_PER_TURN,
        effect=_doll_to_bottom,
    )


card = FossilItemCardDef(
    guid="805bec0f-66ad-5d93-91db-eb373825c1dd",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesPokDoll.Name",
    display_name="Lillie's Pok\u00e9 Doll",
    searchable_by=["Lillie's Pok\u00e9 Doll", "Item"],
    subtypes=["Item"],
    collector_number=267,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    hp=30,
    passive=FossilBodyPassive(),
    abilities=[_doll_ability()],
)
card.prize_count = 0
