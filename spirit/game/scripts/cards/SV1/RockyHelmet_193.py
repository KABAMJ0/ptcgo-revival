from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import retaliate_on_attack

card = PokemonToolCardDef(
    guid="fe9ff5ee-f9ae-5247-afb2-4b36739661a2",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockyHelmet.Name",
    display_name="Rocky Helmet",
    searchable_by=["Rocky Helmet", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=193,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    passive=retaliate_on_attack(2)
)
