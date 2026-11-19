from ptcgo.game.data_utils import PokemonToolCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_EX, is_pokemon_gx
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.data_utils import subtypes_for


class BeastBringerPassive(Passive):
    """With exactly 6 Prizes left, the holder's attack Knocking Out the
    opponent's Active Pokemon-GX or Pokemon-EX takes 1 more Prize card."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or ctx is None or not ctx.is_attack_effect():
            return count
        if pokemon.owning_player_id == holder.owning_player_id:
            return count
        if getattr(ctx, "attacker", None) is not holder:
            return count
        if ctx.board.active_pokemon(pokemon.owning_player_id) is not pokemon:
            return count
        if not (is_pokemon_gx(pokemon) or is_pokemon_EX(pokemon)):
            return count
        if "Ultra Beast" not in subtypes_for(holder.archetype_id):
            return count
        prizes = ctx.board.find_player_area(holder.owning_player_id, "prizePile")
        if prizes is None or len(prizes.children) != 6:
            return count
        return count + 1


card = PokemonToolCardDef(
    guid="46315776-88a1-5d3a-93dc-43ae9ecb11d2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name",
    display_name="Beast Bringer",
    searchable_by=["Beast Bringer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=164,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=BeastBringerPassive(),
)
