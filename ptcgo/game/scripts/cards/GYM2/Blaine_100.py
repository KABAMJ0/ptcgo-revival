from ptcgo.game.card_effects.trainers import attach_energy_spending_free_attachment, basic_energy_of, owned_by
from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities

card = ItemCardDef(
    guid="b52f1787-5bbe-5950-9039-2ce8435f6434",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Blaine.Name",
    display_name="Blaine",
    searchable_by=["Blaine"],
    subtypes=[],
    collector_number=100,
    set_code="GYM2",
    rarity=Rarities.Rare,
    effect=attach_energy_spending_free_attachment(2, basic_energy_of("fire"), owned_by("Blaine"))
)
