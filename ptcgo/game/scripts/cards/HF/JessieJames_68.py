from ptcgo.game.card_effects.trainers import each_player_discards
from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities

card = SupporterCardDef(
    guid="4c177700-8b69-5360-9e46-21af47b77315",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JessieJames.Name",
    display_name="Jessie & James",
    searchable_by=["Jessie & James", "Supporter"],
    subtypes=["Supporter"],
    collector_number=68,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=each_player_discards(2)
)
