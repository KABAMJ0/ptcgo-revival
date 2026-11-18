from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import turn_boost_chosen

card = ItemCardDef(
    guid="2a170ab2-372d-5662-a59d-51aa5e446bd5",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower"],
    subtypes=[],
    collector_number=113,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=turn_boost_chosen(10, active_only=True)
)
