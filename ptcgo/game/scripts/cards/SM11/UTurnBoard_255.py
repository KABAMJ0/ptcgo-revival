from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_retreat_discount

card = PokemonToolCardDef(
    guid="8fdf4d41-7ae5-509e-80f3-d5ff1c04528c",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UTurnBoard.Name",
    display_name="U-Turn Board",
    searchable_by=["U-Turn Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=255,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    passive=holder_retreat_discount(1)
)
