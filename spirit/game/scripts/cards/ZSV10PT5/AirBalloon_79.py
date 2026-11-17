from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_retreat_discount

card = PokemonToolCardDef(
    guid="dfcec98c-debf-52c6-b162-e72b13493c3b",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AirBalloon.Name",
    display_name="Air Balloon",
    searchable_by=["Air Balloon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=79,
    set_code="ZSV10PT5",
    rarity=Rarities.Uncommon,
    passive=holder_retreat_discount(2)
)
