from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_hp_bonus, is_basic_pokemon

card = PokemonToolCardDef(
    guid="6362d92e-544b-52e9-af39-75053a90bb2a",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveryCharm.Name",
    display_name="Bravery Charm",
    searchable_by=["Bravery Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=175,
    set_code="SV7",
    rarity=Rarities.Rare,
    passive=gated_hp_bonus(50, is_basic_pokemon)
)
