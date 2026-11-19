from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.data_utils import Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import entity_name

async def celadon_gym(ctx):
    """Discard an Energy card attached to 1 of your Erika-named Pokemon to
    remove all Special Conditions from it."""
    erika = [p for p in ctx.my_pokemon_in_play()
             if "erika" in (entity_name(p) or "").lower()
             and ctx.attached_energies(p)]
    if not erika:
        return
    chosen = await ctx.choose_pokemon(erika, "Choose an Erika Pokemon")
    if chosen is None:
        return
    energies = ctx.attached_energies(chosen)
    picks = await ctx.choose_cards(energies, 1, minimum=1,
                                   prompt="Discard an Energy card")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.cure_all_conditions(chosen)


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
    ability=Ability(
        title="Celadon City Gym",
        activation=Activations.ONCE_PER_TURN,
        effect=celadon_gym,
    )
)
