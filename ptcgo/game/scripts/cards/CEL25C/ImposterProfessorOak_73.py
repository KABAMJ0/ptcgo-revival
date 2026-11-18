from ptcgo.game.data_utils import ItemCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_shuffle_hand_draw

card = ItemCardDef(
    guid="6c4d9d61-ebc4-59b2-98f1-93f6e11f20eb",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterProfessorOak.Name",
    display_name="Imposter Professor Oak",
    searchable_by=["Imposter Professor Oak"],
    subtypes=[],
    collector_number=73,
    set_code="CEL25C",
    rarity=Rarities.Common,
    effect=opponent_shuffle_hand_draw(7)
)
