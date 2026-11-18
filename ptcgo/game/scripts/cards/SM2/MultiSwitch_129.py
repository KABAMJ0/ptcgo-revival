from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_to_active

card = ItemCardDef(
    guid="0c698d08-3e32-57c7-b9ef-f490af9b53e7",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name",
    display_name="Multi Switch",
    searchable_by=["Multi Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=move_energy_to_active(1)
)
