from ptcgo.game.data_utils import SupporterCardDef, def_for
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import look_top_attach_energy
from ptcgo.game.card_effects.trainers import is_energy_card, named_exactly

_COST_NAMES = ("Dana", "Evelyn", "Nita")


def _morgan_playable(board, player_id):
    """Playable only with Dana, Evelyn and Nita all in hand."""
    hand = board.find_player_area(player_id, "hand")
    names = {(getattr(def_for(c.archetype_id), "display_name", "") or "")
             for c in (hand.children if hand else [])}
    return all(name in names for name in _COST_NAMES)


async def _morgan(ctx):
    """Pay the three named Supporters, then attach any Energy from the top 12."""
    for name in _COST_NAMES:
        pool = [c for c in ctx.hand() if named_exactly(name)(c)]
        if not pool:
            return
        await ctx.discard_cards([pool[0]])
    await look_top_attach_energy(12, is_energy_card, rest="shuffle")(ctx)


card = SupporterCardDef(
    guid="b04c3743-5bbe-51cf-8a7a-da1c7b7beef7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    condition=_morgan_playable,
    effect=_morgan,
)
