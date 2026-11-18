from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import def_for
from ptcgo.game.session.effects import is_pokemon_card

async def _repeat_ball(ctx):
    mine = ctx.my_pokemon_in_play()
    if not mine:
        return
    chosen = await ctx.choose_pokemon(
        mine, "Choose a Pokémon in play") if len(mine) > 1 else mine[0]
    if chosen is None:
        return
    name = getattr(def_for(chosen.archetype_id), "display_name", "") or ""

    def shares_name(card):
        if not is_pokemon_card(card):
            return False
        return (getattr(def_for(card.archetype_id), "display_name", "") or "") == name

    found = await ctx.search_deck(
        shares_name, count=1, minimum=0,
        prompt="Choose a Pokémon with the same name")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="599e6d4f-7a60-578c-a17d-20f2d1c1eef0",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RepeatBall.Name",
    display_name="Repeat Ball",
    searchable_by=["Repeat Ball", "Item"],
    subtypes=["Item"],
    collector_number=136,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    effect=_repeat_ball
)
