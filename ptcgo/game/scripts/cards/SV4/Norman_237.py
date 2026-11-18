from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_if_opponent_active, is_pokemon_ex

card = SupporterCardDef(
    guid="33391e1c-e0c2-5f74-9fef-29bfba166710",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Norman.Name",
    display_name="Norman",
    searchable_by=["Norman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=237,
    set_code="SV4",
    rarity=Rarities.Rare,
    effect=draw_if_opponent_active(is_pokemon_ex, 2, 2)
)
