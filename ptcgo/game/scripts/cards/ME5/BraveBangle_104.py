from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gated_damage_boost, is_pokemon_ex, is_rule_box_free_pokemon

card = PokemonToolCardDef(
    guid="f3d5ffc4-cd8e-5985-9674-aa5d7d7093f1",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveBangle.Name",
    display_name="Brave Bangle",
    searchable_by=["Brave Bangle", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=104,
    set_code="ME5",
    rarity=Rarities.Rare,
    passive=gated_damage_boost(30, is_rule_box_free_pokemon, target=is_pokemon_ex)
)
