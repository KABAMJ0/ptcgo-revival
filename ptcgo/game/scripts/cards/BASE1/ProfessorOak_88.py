from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import discard_hand_draw

card = ItemCardDef(
    guid="ae3252b8-e1cc-5290-9385-a1d6b276ac79",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOak.Name",
    display_name="Professor Oak",
    searchable_by=["Professor Oak"],
    subtypes=[],
    collector_number=88,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=discard_hand_draw(7)
)
