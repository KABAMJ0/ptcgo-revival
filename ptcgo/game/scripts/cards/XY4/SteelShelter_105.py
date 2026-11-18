from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of
from ptcgo.game.card_effects.passives_common import condition_immunity_passive


_METAL = pokemon_of("metal")


def _metal_side(target, carrier):
    """(target, carrier) pred for the stadium passive: a Metal Pokemon."""
    return _METAL(target)


async def _steel_shelter(ctx):
    """Clear the Special Conditions already on every Metal Pokemon in play."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if _METAL(pokemon):
            await ctx.cure_all_conditions(pokemon)


card = StadiumCardDef(
    guid="32608b93-6a75-5185-88d7-2e7ab660357d",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SteelShelter.Name",
    display_name="Steel Shelter",
    searchable_by=["Steel Shelter", "Stadium"],
    subtypes=["Stadium"],
    collector_number=105,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=condition_immunity_passive(protects=_metal_side),
    effect=_steel_shelter,
)
