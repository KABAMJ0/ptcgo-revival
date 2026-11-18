from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import hand_has, is_metal_energy_card, molayne

card = SupporterCardDef(
    guid="4db8befe-b191-5726-a9b3-46d9ff359f7a",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Molayne.Name",
    display_name="Molayne",
    searchable_by=["Molayne", "Supporter"],
    subtypes=["Supporter"],
    collector_number=212,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=molayne(),
    condition=hand_has(is_metal_energy_card, 2)
)
