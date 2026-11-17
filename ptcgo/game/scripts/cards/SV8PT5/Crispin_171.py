from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_split_energy_to_hand_and_attach

card = SupporterCardDef(
    guid="4fcffa86-30b9-5b92-8334-557280907be9",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Crispin.Name",
    display_name="Crispin",
    searchable_by=["Crispin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=171,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    effect=search_split_energy_to_hand_and_attach()
)
