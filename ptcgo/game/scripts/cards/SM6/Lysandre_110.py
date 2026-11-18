from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import lost_zone_per_typed, pokemon_of

card = SupporterCardDef(
    guid="89bf6e51-6769-5f5b-b1b4-f0aec5c9ea0c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lysandre.Name",
    display_name="Lysandre ◇",
    searchable_by=["Lysandre \u25c7", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=110,
    set_code="SM6",
    rarity=Rarities.Rare,
    effect=lost_zone_per_typed(pokemon_of("fire"), 1)
)
