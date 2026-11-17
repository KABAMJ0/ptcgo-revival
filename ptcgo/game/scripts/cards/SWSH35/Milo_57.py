from ptcgo.game.card_effects.trainers import milo
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="545e0881-dd2a-5094-b80d-d64c03f6fad3",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Milo.Name",
    display_name="Milo",
    searchable_by=["Milo", "Supporter"],
    subtypes=["Supporter"],
    collector_number=57,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=milo
)
