from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import mill_own_deck

card = ItemCardDef(
    guid="f2157432-6c82-5d4d-8240-bd1fdc2851b6",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HoleDiggingShovel.Name",
    display_name="Hole-Digging Shovel",
    searchable_by=["Hole-Digging Shovel", "Item"],
    subtypes=["Item"],
    collector_number=74,
    set_code="ME3",
    rarity=Rarities.Common,
    effect=mill_own_deck(2)
)
