from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_is_last


async def blaines_last_resort(ctx):
    await ctx.reveal_hand()
    await ctx.draw_cards(5)


card = ItemCardDef(
    guid="bee093f9-1659-5487-bddb-424a66bb09cd",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastResort.Name",
    display_name="Blaine's Last Resort",
    searchable_by=["Blaine's Last Resort"],
    subtypes=[],
    collector_number=105,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=blaines_last_resort,
    condition=hand_is_last(),
)
