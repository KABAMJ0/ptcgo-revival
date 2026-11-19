from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot


async def _pokemon_park(ctx):
    """A hand attach to the player's own Benched Pokemon removes 1 damage
    counter from it."""
    receiver = ctx.energy_receiver
    if receiver is None or ctx.attaching_player_id != receiver.owning_player_id:
        return
    if is_in_active_spot(receiver):
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
            title='Pokémon Park',
            game_text="Once during each player's turn, when that player attaches an Energy card\nfrom his or her hand to 1 of his or her Benched Pokemon, he or she removes 1\ndamage counter from that Pokemon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_pokemon_park,
        ),
    ],
)
