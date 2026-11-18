from ptcgo.game.data_utils import SupporterCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import AllAbilitiesOffPassive


async def _hex_maniac(ctx):
    """No Abilities anywhere until the end of the opponent's next turn.

    The engine has no board-wide temporary passive: `add_passive_through_
    opponents_turn` hangs a `Passive` on one in-play carrier, and every
    carrier's `blocks_abilities` answers for ALL Pokemon. So the lock is put
    on each Pokemon in play (both sides) and any survivor keeps it on for the
    whole window -- which is what makes the printed "(this includes cards that
    come into play on that turn)" work for late arrivals.
    """
    lock = AllAbilitiesOffPassive()
    for player_id in (ctx.player_id, ctx.opponent_id):
        for pokemon in ctx.board.pokemon_in_play(player_id):
            ctx.add_passive_through_opponents_turn(pokemon, lock)


card = SupporterCardDef(
    guid="20a7e210-a23e-591b-96d4-807b0e9c6c50",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HexManiac.Name",
    display_name="Hex Maniac",
    searchable_by=["Hex Maniac", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    effect=_hex_maniac
)
