from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import discard_hand_draw

card = ItemCardDef(
    guid="2843a9a2-e8a6-5563-bbdb-368206b29ae9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOak.Name",
    display_name="Professor Oak",
    searchable_by=["Professor Oak"],
    subtypes=[],
    collector_number=116,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(7)
)
