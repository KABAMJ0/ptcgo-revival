from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import search_split_energy_to_hand_and_attach

card = SupporterCardDef(
    guid="20023685-f894-5830-8e4c-943de44f07ac",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Crispin.Name",
    display_name="Crispin",
    searchable_by=["Crispin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=164,
    set_code="SV7",
    rarity=Rarities.Rare,
    effect=search_split_energy_to_hand_and_attach()
)
