from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import search_split_energy_to_hand_and_attach

card = SupporterCardDef(
    guid="bdef071d-0d3f-514f-a1d0-1b029a842895",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Crispin.Name",
    display_name="Crispin",
    searchable_by=["Crispin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    effect=search_split_energy_to_hand_and_attach()
)
