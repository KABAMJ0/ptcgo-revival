from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    ends_turn_after, fossil_evolution_card, stadium_ability,
)


async def _research_lab(ctx):
    picks = await ctx.search_deck(
        fossil_evolution_card, count=2, minimum=0,
        prompt="Choose up to 2 Pok\u00e9mon that evolve from Unidentified Fossil")
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = StadiumCardDef(
    guid="1a8505d9-1d49-5ac0-b6f2-167cf497904d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonResearchLab.Name",
    display_name="Pok\u00e9mon Research Lab",
    searchable_by=["Pok\u00e9mon Research Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=205,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    ability=stadium_ability(
        "Pok\u00e9mon Research Lab", ends_turn_after(_research_lab)),
)
