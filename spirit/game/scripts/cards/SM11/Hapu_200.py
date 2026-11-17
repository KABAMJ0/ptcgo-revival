from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b4863af3-49c5-51d7-af22-66305e1bba37",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hapu.Name",
    display_name="Hapu",
    searchable_by=["Hapu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=200,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
