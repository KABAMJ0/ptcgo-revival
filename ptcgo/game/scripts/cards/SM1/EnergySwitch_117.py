from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="181ca5af-d3d9-5444-9dc5-4ba89efda8a5",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
