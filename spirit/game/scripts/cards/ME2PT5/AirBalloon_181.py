from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_retreat_discount

card = PokemonToolCardDef(
    guid="6dc14098-0caf-57c0-8b6a-e32b424ac9b4",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AirBalloon.Name",
    display_name="Air Balloon",
    searchable_by=["Air Balloon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=181,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    passive=holder_retreat_discount(2)
)
