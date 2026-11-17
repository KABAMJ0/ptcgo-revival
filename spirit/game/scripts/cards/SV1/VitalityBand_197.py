from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_damage_boost

card = PokemonToolCardDef(
    guid="f0e969c0-a61e-57eb-bf1b-e9a68902c3db",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VitalityBand.Name",
    display_name="Vitality Band",
    searchable_by=["Vitality Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=197,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    passive=holder_damage_boost(10)
)
