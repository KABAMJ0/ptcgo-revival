from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_basic_energy

card = ItemCardDef(
    guid="846c222c-33ab-5929-9d29-b7de59dcd949",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=61,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=move_basic_energy(predicate=is_basic_energy_card)
)
