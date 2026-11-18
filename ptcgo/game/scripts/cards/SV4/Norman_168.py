from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import draw_if_opponent_active, is_pokemon_ex

card = SupporterCardDef(
    guid="f35175d6-7f35-5101-8b34-fc7ae1a23b92",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Norman.Name",
    display_name="Norman",
    searchable_by=["Norman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    effect=draw_if_opponent_active(is_pokemon_ex, 2, 2)
)
