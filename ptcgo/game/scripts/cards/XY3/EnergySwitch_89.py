from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="57417a79-c9bc-515f-9810-0e32a2d51b9d",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
