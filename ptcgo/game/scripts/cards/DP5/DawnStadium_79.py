from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of


_GRASS_ON_ATTACH = pokemon_of("grass")
_WATER_ON_ATTACH = pokemon_of("water")


async def _dawn_stadium(ctx):
    """An Energy attached to a Grass or Water Pokemon heals it 10 and clears
    its Special Conditions."""
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    if not (_GRASS_ON_ATTACH(receiver) or _WATER_ON_ATTACH(receiver)):
        return
    await ctx.heal(10, receiver)
    await ctx.cure_all_conditions(receiver)


card = StadiumCardDef(
    guid="5afc6588-d84c-5368-9768-e2deea51b10d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DawnStadium.Name",
    display_name="Dawn Stadium",
    searchable_by=["Dawn Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Dawn Stadium',
            game_text='Whenever any player attaches an Energy card from his or her hand to a Grass\nPokemon or a Water Pokemon, remove 1 damage counter and all Special Conditions\nfrom that Pokemon.',
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_dawn_stadium,
        ),
    ],
)
