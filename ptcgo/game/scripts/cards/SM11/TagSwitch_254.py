from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_from_holder, pokemon_of_subtype

card = ItemCardDef(
    guid="c9760d1a-d5ec-50d6-be73-46592e9b8d57",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagSwitch.Name",
    display_name="Tag Switch",
    searchable_by=["Tag Switch", "Item"],
    subtypes=["Item"],
    collector_number=254,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    effect=move_energy_from_holder(pokemon_of_subtype("TAG TEAM"), 2)
)
