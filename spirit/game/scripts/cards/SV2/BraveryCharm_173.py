from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_hp_bonus, is_basic_pokemon

card = PokemonToolCardDef(
    guid="7922e84a-8cc7-5815-b52d-5939f3419606",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveryCharm.Name",
    display_name="Bravery Charm",
    searchable_by=["Bravery Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=173,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    passive=gated_hp_bonus(50, is_basic_pokemon)
)
