from ptcgo.game.data_utils import StadiumCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of


_CAVE_TYPES = tuple(pokemon_of(name) for name in ("water", "fighting", "metal"))


async def _island_cave(ctx):
    """An Energy attached to a Water, Fighting or Metal Pokemon clears its
    Special Conditions."""
    receiver = ctx.energy_receiver
    if receiver is not None and any(check(receiver) for check in _CAVE_TYPES):
        await ctx.cure_all_conditions(receiver)


card = StadiumCardDef(
    guid="92a822a3-e4e5-5d8e-b154-743db8902ecf",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandCave.Name",
    display_name="Island Cave",
    searchable_by=["Island Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title='Island Cave',
            game_text='Whenever any player attaches an Energy card from his or her hand to a Water\nPokemon, Fighting Pokemon, or Metal Pokemon, remove any Special Conditions from\nthat Pokemon.',
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_island_cave,
        ),
    ],
)
