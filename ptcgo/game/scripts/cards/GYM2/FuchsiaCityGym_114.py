from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import named, stadium_ability
from ptcgo.game.session.effects import full_stack

_KOGA = named("koga")


async def fuchsia_city_gym_shuffle(ctx):
    """Once during each player's turn, that player may flip a coin; on heads
    they may shuffle a Pokemon with Koga in its name and its attachments into
    their deck."""
    heads = await ctx.flip_coins(1, title="Fuchsia City Gym")
    if not heads or not heads[0]:
        return
    candidates = [p for p in ctx.my_pokemon_in_play() if _KOGA(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Koga Pokémon to shuffle into your deck",
        optional=True)
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = StadiumCardDef(
    guid="4115c0f1-efc5-53b0-b8a4-4b043ae81c7c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FuchsiaCityGym.Name",
    display_name="Fuchsia City Gym",
    searchable_by=["Fuchsia City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Fuchsia City Gym", fuchsia_city_gym_shuffle)
)
