from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_per_subtype

card = SupporterCardDef(
    guid="d0e13667-4c6c-52ca-9f05-777367508a3f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jett.Name",
    display_name="Jett",
    searchable_by=["Jett", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    effect=draw_per_subtype("Mega Evolution", 1, opponent=True)
)
