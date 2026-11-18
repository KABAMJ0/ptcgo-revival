from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gated_retreat_free, is_stage_two

card = PokemonToolCardDef(
    guid="6f33598d-f004-59d4-b0e4-39ad40a09bea",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BigAirBalloon.Name",
    display_name="Big Air Balloon",
    searchable_by=["Big Air Balloon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=155,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    passive=gated_retreat_free(is_stage_two)
)
