from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import gated_damage_boost, is_pokemon_ex, is_rule_box_free_pokemon

card = PokemonToolCardDef(
    guid="5c528680-2b43-5eb1-9abf-e1a3fa2073ef",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BraveBangle.Name",
    display_name="Brave Bangle",
    searchable_by=["Brave Bangle", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=80,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    passive=gated_damage_boost(30, is_rule_box_free_pokemon, target=is_pokemon_ex)
)
