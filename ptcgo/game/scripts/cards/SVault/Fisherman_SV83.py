from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="1ed0d286-2d5e-55d5-a48d-3a5dab10626e",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="SVault",
    rarity=Rarities.RareUltra,
    effect=unimplemented
)
