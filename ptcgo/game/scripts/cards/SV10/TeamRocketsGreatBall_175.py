from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import all_of, card_named_contains, is_basic_pokemon, is_evolution_pokemon


async def team_rockets_great_ball(ctx):
    """Heads: an Evolution Team Rocket's Pokemon; tails: a Basic one."""
    heads = (await ctx.flip_coins(1, "Team Rocket's Great Ball"))[0]
    kind = is_evolution_pokemon if heads else is_basic_pokemon
    found = await ctx.search_deck(
        all_of(card_named_contains("Team Rocket"), kind), count=1, minimum=0,
        prompt="Choose a Team Rocket's Pok\u00e9mon to put into your hand")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="c865accf-3750-57ca-b3ae-9a5d4ec1ce80",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsGreatBall.Name",
    display_name="Team Rocket's Great Ball",
    searchable_by=["Team Rocket's Great Ball", "Item"],
    subtypes=["Item"],
    collector_number=175,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    effect=team_rockets_great_ball,
)
