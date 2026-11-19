from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities


async def pokemon_park(ctx):
    """Energy from hand onto a Benched Pokemon: remove 1 damage counter from it."""
    receiver = ctx.energy_receiver
    if receiver is None or ctx.attaching_player_id != ctx.player_id:
        return
    if receiver not in ctx.my_bench():
        return
    await ctx.heal(10, receiver)


card = StadiumCardDef(
    guid="145ab58a-76d5-55a1-b554-f02441d7b505",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokmonPark.Name",
    display_name="Pokémon Park",
    searchable_by=["Pok\u00e9mon Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=10,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Pok\u00e9mon Park",
            game_text="Once during each player's turn, when that player attaches an Energy card from his or her hand to 1 of his or her Benched Pok\u00e9mon, he or she removes 1 damage counter from that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=pokemon_park,
        ),
    ],
)
