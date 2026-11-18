from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_boost_per_prize_taken, pokemon_of_subtype

card = PokemonToolCardDef(
    guid="b3138bdc-662a-53b3-b63f-dbf4ab9d0414",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Beastite.Name",
    display_name="Beastite",
    searchable_by=["Beastite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=185,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    passive=holder_boost_per_prize_taken(10, pokemon_of_subtype("Ultra Beast"))
)
