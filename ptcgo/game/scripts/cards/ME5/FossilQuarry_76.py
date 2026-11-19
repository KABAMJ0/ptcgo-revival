from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.data_utils import Ability, Activations, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_bench


def antique_item(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return "antique" in (getattr(definition, "display_name", "") or "").lower()

async def fossil_quarry(ctx):
    """Search your deck for up to 2 Item cards with "Antique" in their name and
    put them onto your Bench."""
    await search_to_bench(antique_item, count=2)(ctx)


card = StadiumCardDef(
    guid="969b4c1d-8cec-5939-9ffc-a80d4237debf",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilQuarry.Name",
    display_name="Fossil Quarry",
    searchable_by=["Fossil Quarry", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Fossil Quarry",
        activation=Activations.ONCE_PER_TURN,
        effect=fossil_quarry,
    )
)
