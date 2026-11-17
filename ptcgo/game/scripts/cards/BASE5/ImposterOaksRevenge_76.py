from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import opponent_shuffle_hand_draw, with_discard_cost

card = ItemCardDef(
    guid="649ff12a-4b3e-52ca-9ad6-840072930d2f",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ImposterOaksRevenge.Name",
    display_name="Imposter Oak's Revenge",
    searchable_by=["Imposter Oak's Revenge"],
    subtypes=[],
    collector_number=76,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    effect=with_discard_cost(1, opponent_shuffle_hand_draw(4))
)
