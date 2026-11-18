from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_subtype

card = ItemCardDef(
    guid="ad1ca31c-beb6-54df-a1de-88bc52c28372",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AwakeningDrum.Name",
    display_name="Awakening Drum",
    searchable_by=["Awakening Drum", "Item", "Ancient", "ACE SPEC"],
    subtypes=["Item", "Ancient", "ACE SPEC"],
    collector_number=141,
    set_code="SV5",
    rarity=Rarities.Rare,
    effect=draw_per_subtype("Ancient", 1)
)
