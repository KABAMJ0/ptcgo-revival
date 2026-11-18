from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="69ab3162-be0e-5a32-afb0-59a1ad2d76fa",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
