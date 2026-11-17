from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import draw_per_opponent_pokemon, hand_at_most

card = SupporterCardDef(
    guid="85226b04-9e88-5572-b57a-3e3da3f50665",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="HF",
    rarity=Rarities.Rare,
    effect=draw_per_opponent_pokemon(1), condition=hand_at_most(4)
)
