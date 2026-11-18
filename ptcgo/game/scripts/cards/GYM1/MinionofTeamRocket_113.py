from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import full_stack


async def minion_of_team_rocket(ctx):
    """Flip 2 coins: both heads returns a Benched opponent Pokemon and
    everything attached to it to their hand; anything else ends your turn."""
    heads = await ctx.flip_coins(2, title="Minion of Team Rocket")
    if all(heads):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = (await ctx.choose_pokemon(bench, "Choose a Benched Pokemon to return")
                  if len(bench) > 1 else bench[0])
        if target is not None:
            await ctx.put_in_hand(full_stack(target), reveal=False)
        return
    ctx.ends_turn = True


card = ItemCardDef(
    guid="b8630af1-bc33-5a85-b609-2ce96111429d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MinionofTeamRocket.Name",
    display_name="Minion of Team Rocket",
    searchable_by=["Minion of Team Rocket"],
    subtypes=[],
    collector_number=113,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=minion_of_team_rocket
)
