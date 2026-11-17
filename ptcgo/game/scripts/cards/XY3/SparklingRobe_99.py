from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import holder_condition_immunity

card = PokemonToolCardDef(
    guid="f05087b3-ca20-5ec4-b850-b5db64d3d28b",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SparklingRobe.Name",
    display_name="Sparkling Robe",
    searchable_by=["Sparkling Robe", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=holder_condition_immunity()
)
