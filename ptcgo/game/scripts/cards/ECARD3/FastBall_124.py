from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_evolution_pokemon

async def _fast_ball(ctx):
    for card in reversed(ctx.deck()):
        if is_evolution_pokemon(card):
            await ctx.put_in_hand([card], reveal=True)
            break
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="b061d93d-7948-5f3f-9d2b-9528b82c0ad1",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FastBall.Name",
    display_name="Fast Ball",
    searchable_by=["Fast Ball"],
    subtypes=[],
    collector_number=124,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=_fast_ball
)
