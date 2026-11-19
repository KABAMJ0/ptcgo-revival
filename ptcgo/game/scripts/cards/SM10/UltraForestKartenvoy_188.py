from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_of_subtype


async def ultra_forest_kartenvoy(ctx):
    """During this turn, your Ultra Beasts' attacks aren't affected by effects
    on your opponent's Active Pokemon."""
    for pokemon in ctx.my_pokemon_in_play():
        if pokemon_of_subtype("Ultra Beast")(pokemon):
            ctx.ignore_own_target_effects(pokemon)


card = SupporterCardDef(
    guid="fe8c8dc0-70d8-5b82-a12b-981517ad54e0",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraForestKartenvoy.Name",
    display_name="Ultra Forest Kartenvoy",
    searchable_by=["Ultra Forest Kartenvoy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=ultra_forest_kartenvoy
)
