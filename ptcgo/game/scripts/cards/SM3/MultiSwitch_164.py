from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import move_energy_to_active

card = ItemCardDef(
    guid="cb41a083-4781-5f35-b326-c45f1062f26d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name",
    display_name="Multi Switch",
    searchable_by=["Multi Switch", "Item"],
    subtypes=["Item"],
    collector_number=164,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    effect=move_energy_to_active(1)
)
