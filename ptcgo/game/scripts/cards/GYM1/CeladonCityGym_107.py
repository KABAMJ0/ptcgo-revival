from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import card_named_any, stadium_ability


_ERIKA = card_named_any(["Erika"])


async def _celadon_city_gym(ctx):
    """Once each turn: the acting player may discard an Energy from 1 of their
    Pokemon with Erika in its name to clear its Special Conditions."""
    pool = [p for p in ctx.my_pokemon_in_play()
            if _ERIKA(p) and ctx.attached_energies(p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Choose an Erika's Pokemon") if len(pool) > 1 else pool[0]
    if target is None:
        return
    picks = await ctx.choose_cards(
        ctx.attached_energies(target), 1, minimum=1,
        prompt="Discard an Energy card from that Pokemon")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.cure_all_conditions(target)


card = StadiumCardDef(
    guid="332ba831-6589-57d8-b8ce-a98c30f95580",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeladonCityGym.Name",
    display_name="Celadon City Gym",
    searchable_by=["Celadon City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=107,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    ability=stadium_ability("Celadon City Gym", _celadon_city_gym),
)
