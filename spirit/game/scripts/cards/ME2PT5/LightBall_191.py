from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import gated_damage_boost, is_pokemon_ex, named_rule_box

card = PokemonToolCardDef(
    guid="44d6411a-7ebc-54b5-b590-8ce237cc822b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LightBall.Name",
    display_name="Light Ball",
    searchable_by=["Light Ball", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=191,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    passive=gated_damage_boost(50, named_rule_box("pikachu", "ex"), target=is_pokemon_ex)
)
