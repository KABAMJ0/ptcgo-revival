from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.models.board import PokemonEntity
from ptcgo.game.card_effects.trainers import pokemon_of_subtype
from ptcgo.game.session.passives import Passive

_is_tera = pokemon_of_subtype("Tera")

def _in_play_for(carrier):
    """Every in-play Pokemon, found by walking the board from the carrier."""
    node = carrier
    while node.parent is not None:
        node = node.parent
    stack, areas = [node], []
    while stack:
        current = stack.pop()
        for child in getattr(current, "children", None) or []:
            if child.get_attribute(AttrID.NAME) in ("bench", "activePokemonArea"):
                areas.append(child)
            stack.append(child)
    return [mon for area in areas for mon in area.children
            if isinstance(mon, PokemonEntity)]


class AreaZeroBenchPassive(Passive):
    """A player with any Tera Pokemon in play may have 8 on the Bench. The
    engine's bench-capacity enforcement discards back down to 5 when the Tera
    Pokemon or the Stadium leaves play."""

    def bench_capacity(self, player_id, carrier):
        return 8 if any(mon.owning_player_id == player_id and _is_tera(mon)
                    for mon in _in_play_for(carrier)) else None


card = StadiumCardDef(
    guid="4c338f0a-4bb0-5912-aecc-7f3456ecd2be",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AreaZeroUnderdepths.Name",
    display_name="Area Zero Underdepths",
    searchable_by=["Area Zero Underdepths", "Stadium"],
    subtypes=["Stadium"],
    collector_number=174,
    set_code="SV7",
    rarity=Rarities.Rare,
    passive=AreaZeroBenchPassive(),
)
