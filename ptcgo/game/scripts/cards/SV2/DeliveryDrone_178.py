from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import flip_search_per_head

card = ItemCardDef(
    guid="9836718c-e866-5345-904b-a1019a13034a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DeliveryDrone.Name",
    display_name="Delivery Drone",
    searchable_by=["Delivery Drone", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    effect=flip_search_per_head(2, None, 1, both=True)
)
