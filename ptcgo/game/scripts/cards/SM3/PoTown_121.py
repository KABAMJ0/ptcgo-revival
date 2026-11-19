from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities


async def po_town(ctx):
    """Any player evolves from hand: 3 damage counters on the new Pokemon."""
    evolved = ctx.evolved_pokemon
    if evolved is None:
        return
    await ctx.deal_damage(30, target=evolved, apply_modifiers=False,
                          as_counters=True)


card = StadiumCardDef(
    guid="47e7adfc-ca5b-5eaf-ab1e-cf478e51515d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PoTown.Name",
    display_name="Po Town",
    searchable_by=["Po Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=121,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Po Town",
            game_text="Whenever any player plays a Pok\u00e9mon from their hand to evolve 1 of their Pok\u00e9mon, put 3 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=po_town,
        ),
    ],
)
