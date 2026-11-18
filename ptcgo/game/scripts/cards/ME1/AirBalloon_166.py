from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_retreat_discount

card = PokemonToolCardDef(
    guid="87091492-b9f6-5319-952e-756ea13aa0e2",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AirBalloon.Name",
    display_name="Air Balloon",
    searchable_by=["Air Balloon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=166,
    set_code="ME1",
    rarity=Rarities.Rare,
    passive=holder_retreat_discount(2)
)
