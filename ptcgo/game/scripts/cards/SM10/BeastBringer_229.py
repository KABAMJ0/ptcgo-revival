from ptcgo.game.data_utils import PokemonToolCardDef, subtypes_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import carrier_pokemon
from ptcgo.game.card_effects.trainers import is_pokemon_EX, is_pokemon_gx
from ptcgo.game.session.passives import Passive

class _BeastBringerPrize(Passive):
    """Exact 6 Prizes left, and the Ultra Beast holding this Tool's attack took
    the opponent's Active Pokemon-GX/EX down: take 1 more Prize card."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or ctx.attacker is not holder:
            return count
        if holder.owning_player_id == pokemon.owning_player_id:
            return count
        board = ctx.board
        if board.active_pokemon(pokemon.owning_player_id) is not pokemon:
            return count
        if not (is_pokemon_gx(pokemon) or is_pokemon_EX(pokemon)):
            return count
        if "ultra beast" not in [s.lower()
                                 for s in subtypes_for(holder.archetype_id)]:
            return count
        prizes = board.find_player_area(ctx.player_id, "prizePile")
        if prizes is None or len(prizes.children) != 6:
            return count
        return count + 1


card = PokemonToolCardDef(
    guid="83d5f1c8-103a-5aad-af36-0fc821c360f5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name",
    display_name="Beast Bringer",
    searchable_by=["Beast Bringer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=229,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    passive=_BeastBringerPrize(),
)
