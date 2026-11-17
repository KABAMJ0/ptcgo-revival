from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="96c6a5cc-e7b0-5c8b-bd0a-f63690b32aba",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksNewTheory.Name",
    display_name="Professor Oak's New Theory",
    searchable_by=["Professor Oak's New Theory", "Supporter"],
    subtypes=["Supporter"],
    collector_number=101,
    set_code="HGSS1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(6)
)
