from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_damage_boost

card = ItemCardDef(
    guid="15ba7894-6949-50f2-ae3f-976e87d8615f",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    effect=turn_damage_boost(10)
)
