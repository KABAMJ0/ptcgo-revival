from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_special_between_opponents

card = ItemCardDef(
    guid="3cedc8b5-8c92-59a5-95f4-94853e06f4ed",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name",
    display_name="Eneporter",
    searchable_by=["Eneporter", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    effect=move_energy_special_between_opponents(1)
)
