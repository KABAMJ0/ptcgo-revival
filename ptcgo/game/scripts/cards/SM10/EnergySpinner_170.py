from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, search_going_second

card = ItemCardDef(
    guid="db1ba32a-1034-5a63-b73d-1597c45a988e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySpinner.Name",
    display_name="Energy Spinner",
    searchable_by=["Energy Spinner", "Item"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    effect=search_going_second(is_basic_energy_card, 1, 3)
)
