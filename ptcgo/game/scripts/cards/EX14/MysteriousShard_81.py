from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import (
    is_pokemon_card, is_pokemon_ex, prevents_all_from,
    tool_discard_after_opponents_turn,
)


def _not_pokemon_ex(card):
    return is_pokemon_card(card) and not is_pokemon_ex(card)


card = PokemonToolCardDef(
    guid="3d3e002e-1072-5ad8-993d-8a3ab7c9ccd3",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousShard.Name",
    display_name="Mysterious Shard",
    searchable_by=["Mysterious Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=prevents_all_from(attacker=is_pokemon_ex, effects_too=True),
    granted_abilities=[tool_discard_after_opponents_turn("Mysterious Shard")],
    attach_to=_not_pokemon_ex
)
