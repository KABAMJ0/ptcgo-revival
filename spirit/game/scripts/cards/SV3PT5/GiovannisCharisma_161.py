from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_energy_to_hand_then_attach

card = SupporterCardDef(
    guid="d7db8c35-7eef-5a9a-a11b-bbc9b126fb4b",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisCharisma.Name",
    display_name="Giovanni's Charisma",
    searchable_by=["Giovanni's Charisma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    effect=opponent_energy_to_hand_then_attach()
)
