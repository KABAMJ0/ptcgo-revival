from ptcgo.game.data_utils import SupporterCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import search_split_energy_to_hand_and_attach

card = SupporterCardDef(
    guid="a5d8e7c6-f866-5f5f-ba84-da93fe203975",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Crispin.Name",
    display_name="Crispin",
    searchable_by=["Crispin", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="SV8PT5",
    rarity=Rarities.Uncommon,
    effect=search_split_energy_to_hand_and_attach()
)
