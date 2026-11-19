from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.data_utils import Ability, Activations, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.effects import full_stack
from ptcgo.game.card_effects.support_common import entity_name

async def fuchsia_gym(ctx):
    """Flip a coin. If heads, shuffle 1 of your Koga-named Pokemon and its
    attached cards into your deck."""
    results = await ctx.flip_coins(1, "Fuchsia City Gym")
    if not (results and all(results)):
        return
    koga = [p for p in ctx.my_pokemon_in_play()
            if "koga" in (entity_name(p) or "").lower()]
    if not koga:
        return
    chosen = await ctx.choose_pokemon(koga, "Choose a Koga Pokemon to shuffle in")
    if chosen is not None:
        await ctx.shuffle_into_deck(full_stack(chosen))


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
    ability=Ability(
        title="Fuchsia City Gym",
        activation=Activations.ONCE_PER_TURN,
        effect=fuchsia_gym,
    )
)
