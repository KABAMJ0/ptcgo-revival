from ptcgo.game.data_utils import SupporterCardDef, evolves_from
from ptcgo.game.attributes import AttrID, Rarities


async def _wallys_training(ctx):
    active = ctx.my_active()
    if active is None:
        return
    logic_name = active.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def evolving_from_active(card):
        return bool(logic_name) and evolves_from(
            getattr(card, "archetype_id", None) or "", logic_name)

    picks = await ctx.search_deck(
        evolving_from_active, count=1, minimum=0,
        prompt="Choose an Evolution card for your Active Pok\u00e9mon")
    if picks:
        await ctx.evolve_pokemon(active, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="1ee6d896-ba61-59ee-b459-d49a8a49f6cc",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WallysTraining.Name",
    display_name="Wally's Training",
    searchable_by=["Wally's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="EX9",
    rarity=Rarities.Uncommon,
    effect=_wallys_training
)
