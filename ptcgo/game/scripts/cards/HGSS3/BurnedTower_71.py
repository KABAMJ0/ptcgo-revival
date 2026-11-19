from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.data_utils import Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import is_basic_energy
from ptcgo.game.card_effects.support_common import recover_from_discard

async def burned_tower(ctx):
    """Flip a coin. If heads, search your discard pile for a basic Energy card
    and put it into your hand."""
    results = await ctx.flip_coins(1, "Burned Tower")
    if not (results and all(results)):
        return
    await recover_from_discard(is_basic_energy, count=1, reveal=True)(ctx)


card = StadiumCardDef(
    guid="cc04ff4f-1f85-5756-a89b-1280113a5999",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurnedTower.Name",
    display_name="Burned Tower",
    searchable_by=["Burned Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=71,
    set_code="HGSS3",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Burned Tower",
        activation=Activations.ONCE_PER_TURN,
        effect=burned_tower,
    )
)
