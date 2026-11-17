from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import opponent_energy_to_hand_then_attach

card = SupporterCardDef(
    guid="061d1781-a607-56e1-93fc-57a3292e4e5f",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisCharisma.Name",
    display_name="Giovanni's Charisma",
    searchable_by=["Giovanni's Charisma", "Supporter"],
    subtypes=["Supporter"],
    collector_number=197,
    set_code="SV3PT5",
    rarity=Rarities.Rare,
    effect=opponent_energy_to_hand_then_attach()
)
