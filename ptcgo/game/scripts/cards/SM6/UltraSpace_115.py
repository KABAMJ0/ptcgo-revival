from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import Ability, Activations
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype


def ultra_beast(card) -> bool:
    return has_pokemon_subtype(card, "Ultra Beast")

async def ultra_space(ctx):
    """Search your deck for an Ultra Beast, reveal it, put it into your hand."""
    await search_to_hand(ultra_beast, count=1, reveal=True)(ctx)


card = StadiumCardDef(
    guid="275ec1de-d82c-5643-8416-eb4529477822",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraSpace.Name",
    display_name="Ultra Space",
    searchable_by=["Ultra Space", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Ultra Space",
        activation=Activations.ONCE_PER_TURN,
        effect=ultra_space,
    )
)
