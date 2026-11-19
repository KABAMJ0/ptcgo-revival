from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import Ability, Activations
from ptcgo.game.card_effects.trainers import evolve_from_deck_matching

async def grand_tree(ctx):
    """Search your deck for a Stage 1 that evolves from one of your Basic
    Pokemon and put it onto that Pokemon to evolve it."""
    await evolve_from_deck_matching()(ctx)


card = StadiumCardDef(
    guid="f518ed37-8af1-56ba-920f-cecc5462b4b0",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrandTree.Name",
    display_name="Grand Tree",
    searchable_by=["Grand Tree", "Stadium", "ACE SPEC"],
    subtypes=["Stadium", "ACE SPEC"],
    collector_number=136,
    set_code="SV7",
    rarity=Rarities.Rare,
    ability=Ability(
        title="Grand Tree",
        activation=Activations.ONCE_PER_TURN,
        effect=grand_tree,
    )
)
