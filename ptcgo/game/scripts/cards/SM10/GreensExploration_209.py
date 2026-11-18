from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_trainer_card, no_pokemon_with_abilities

card = SupporterCardDef(
    guid="73897bc6-10ad-52d5-a622-e1ef9b811e14",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_trainer_card, count=2), condition=no_pokemon_with_abilities()
)
