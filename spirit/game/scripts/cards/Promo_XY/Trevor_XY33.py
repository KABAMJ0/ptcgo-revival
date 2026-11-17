from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="215733d5-9be6-58bd-a058-252d1a91c14f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Trevor.Name",
    display_name="Trevor",
    searchable_by=["Trevor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=33,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=unimplemented
)
