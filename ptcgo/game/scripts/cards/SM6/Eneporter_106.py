from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_special_between_opponents

card = ItemCardDef(
    guid="e4d8a65f-5efa-58de-97f0-f0528cbe0716",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name",
    display_name="Eneporter",
    searchable_by=["Eneporter", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    effect=move_energy_special_between_opponents(1)
)
