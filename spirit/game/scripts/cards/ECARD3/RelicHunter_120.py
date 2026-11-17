from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="426d434b-96f3-56a4-9227-e7ef2e735d67",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RelicHunter.Name",
    display_name="Relic Hunter",
    searchable_by=["Relic Hunter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=unimplemented
)
