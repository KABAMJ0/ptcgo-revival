from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9e454373-0ca6-5331-a74e-5efac6f13590",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Youngster.Name",
    display_name="Youngster",
    searchable_by=["Youngster", "Supporter"],
    subtypes=["Supporter"],
    collector_number=198,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
