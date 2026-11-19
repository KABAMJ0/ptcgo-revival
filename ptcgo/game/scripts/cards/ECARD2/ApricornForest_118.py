from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.card_effects.trainers import (
    is_basic_energy_card,
    is_basic_pokemon,
    stadium_ability,
)


async def _apricorn_forest(ctx):
    if len(ctx.my_bench()) >= ctx.bench_limit():
        return
    if not (await ctx.flip_coins(1, title="Apricorn Forest"))[0]:
        return
    energies = [card for card in ctx.hand() if is_basic_energy_card(card)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose a basic Energy card to reveal")
    if not picks:
        return
    energy = picks[0]
    await ctx.reveal_cards([energy])
    types = energy.get_attribute(AttrID.POKEMON_TYPES) or []

    def same_type(card):
        if not is_basic_pokemon(card, ctx.board):
            return False
        return any(t in types for t in (card.get_attribute(AttrID.POKEMON_TYPES) or []))

    found = await ctx.search_deck(
        same_type, count=1, minimum=0,
        prompt="Choose a Basic Pok\u00e9mon of the same type",
        slot_prompt="Choose a Basic Pok\u00e9mon of the same type.")
    if found:
        await ctx.bench_pokemon(found[0])
    await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="fbac458b-7552-51ee-a3b2-63c9044f60fe",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornForest.Name",
    display_name="Apricorn Forest",
    searchable_by=["Apricorn Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=118,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    ability=stadium_ability("Apricorn Forest", _apricorn_forest)
)
