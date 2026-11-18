from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_basic_energy_card, move_energy_between_own

card = ItemCardDef(
    guid="e085f783-c8aa-5678-962b-31ab4192df39",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=move_energy_between_own(1, is_basic_energy_card)
)
