from ptcgo.game.card_effects.trainers import is_trainer_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import Attack, SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities


def _no_ability_in_play(board, player_id):
    """`PokemonCardDef.abilities` carries Attacks too, so an Ability here means
    any printed entry that is not an Attack."""
    for pokemon in board.pokemon_in_play(player_id):
        definition = def_for(pokemon.archetype_id)
        if any(not isinstance(entry, Attack)
               for entry in getattr(definition, "abilities", None) or []):
            return False
    return True


card = SupporterCardDef(
    guid="73897bc6-10ad-52d5-a622-e1ef9b811e14",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreensExploration.Name",
    display_name="Green's Exploration",
    searchable_by=["Green's Exploration", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_trainer_card, count=2, minimum=0, reveal=True),
    condition=_no_ability_in_play
)
