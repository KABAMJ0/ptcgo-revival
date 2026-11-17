from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import holder_coin_reroll, pokemon_of

card = PokemonToolCardDef(
    guid="158f69a0-9205-528b-a4bc-464c562c0af9",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BacktrackBadge.Name",
    display_name="Backtrack Badge",
    searchable_by=["Backtrack Badge", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    passive=holder_coin_reroll(pokemon_of("colorless"))
)
