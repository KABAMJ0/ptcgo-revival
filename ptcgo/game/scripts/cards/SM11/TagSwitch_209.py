from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_from_holder, pokemon_of_subtype

card = ItemCardDef(
    guid="33950d93-fcd2-571b-b874-86f31f0ded2e",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TagSwitch.Name",
    display_name="Tag Switch",
    searchable_by=["Tag Switch", "Item"],
    subtypes=["Item"],
    collector_number=209,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=move_energy_from_holder(pokemon_of_subtype("TAG TEAM"), 2)
)
