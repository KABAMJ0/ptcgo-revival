from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="7b5c103a-b1e2-504a-808f-86cd15d3c1f0",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="XY6",
    rarity=Rarities.RareSecret,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
