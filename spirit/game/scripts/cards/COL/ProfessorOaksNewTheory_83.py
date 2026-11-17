from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import shuffle_hand_draw

card = SupporterCardDef(
    guid="ee159102-bab0-570d-9638-85ca853bb554",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksNewTheory.Name",
    display_name="Professor Oak's New Theory",
    searchable_by=["Professor Oak's New Theory", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="COL",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_draw(6)
)
