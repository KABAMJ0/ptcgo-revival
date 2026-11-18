from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="9443de55-1da5-5714-a61a-4de6cabbe2bb",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=173,
    set_code="SV1",
    rarity=Rarities.Common,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
