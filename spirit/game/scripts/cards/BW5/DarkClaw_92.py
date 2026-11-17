from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_damage_boost, pokemon_of

card = PokemonToolCardDef(
    guid="b0c9b3c9-9d9d-55ef-9c08-630e46ecdb3f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkClaw.Name",
    display_name="Dark Claw",
    searchable_by=["Dark Claw", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    passive=gated_damage_boost(20, pokemon_of("darkness"))
)
