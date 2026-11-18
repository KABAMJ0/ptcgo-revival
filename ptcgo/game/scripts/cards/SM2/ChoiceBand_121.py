from ptcgo.game.data_utils import PokemonToolCardDef, unimplemented
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import any_of, holder_damage_boost, is_pokemon_ex, is_pokemon_gx

card = PokemonToolCardDef(
    guid="153670d3-a44c-5c04-a706-4d49d0df9153",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChoiceBand.Name",
    display_name="Choice Band",
    searchable_by=["Choice Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=121,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    passive=holder_damage_boost(30, target_pred=any_of(is_pokemon_gx, is_pokemon_ex))
)
