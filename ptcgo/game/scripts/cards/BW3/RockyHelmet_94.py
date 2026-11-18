from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import retaliate_on_attack

card = PokemonToolCardDef(
    guid="977a46b2-32b3-5da8-b89b-937e69d7c667",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockyHelmet.Name",
    display_name="Rocky Helmet",
    searchable_by=["Rocky Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=94,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    passive=retaliate_on_attack(2)
)
