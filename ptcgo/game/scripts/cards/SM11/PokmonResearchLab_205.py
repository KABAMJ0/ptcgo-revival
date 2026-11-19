from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.data_utils import Ability, Activations, def_for
from ptcgo.game.card_effects.support_common import search_to_bench


def evolves_from_unidentified_fossil(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return "unidentified fossil" in (
        (getattr(definition, "evolves_from", "") or "").lower())

async def research_lab(ctx):
    """Search your deck for up to 2 Pokemon that evolve from Unidentified
    Fossil, put them onto your Bench, then this turn ends."""
    await search_to_bench(evolves_from_unidentified_fossil, count=2)(ctx)


card = StadiumCardDef(
    guid="1a8505d9-1d49-5ac0-b6f2-167cf497904d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonResearchLab.Name",
    display_name="Pokémon Research Lab",
    searchable_by=["Pok\u00e9mon Research Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=205,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Pokemon Research Lab",
        activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
        effect=research_lab,
    )
)
