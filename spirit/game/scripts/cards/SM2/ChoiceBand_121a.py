from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import any_of, holder_damage_boost, is_pokemon_ex, is_pokemon_gx

card = PokemonToolCardDef(
    guid="e1cb70ff-d0a8-5549-8435-8641dcc11ef7",
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
