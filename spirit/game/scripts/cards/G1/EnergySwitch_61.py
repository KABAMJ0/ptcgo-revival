from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="846c222c-33ab-5929-9d29-b7de59dcd949",
    key="G1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=61,
    set_code="G1",
    rarity=Rarities.Uncommon,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
