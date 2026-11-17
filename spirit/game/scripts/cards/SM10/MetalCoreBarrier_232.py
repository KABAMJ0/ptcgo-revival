from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import pokemon_of, takes_less_from

card = PokemonToolCardDef(
    guid="cef2d1c4-371e-5489-b6dd-f1246929f4a2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCoreBarrier.Name",
    display_name="Metal Core Barrier",
    searchable_by=["Metal Core Barrier", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=232,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    passive=takes_less_from(70, pokemon_of("metal"))
)
