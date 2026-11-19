from ptcgo.game.attributes import (
    CLIENT_SPECIAL_CONDITION_NAMES, Rarities, SpecialConditions,
)
from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.session.passives import Passive

POISONED = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]


class DustIslandPassive(Passive):
    """A Poisoned Active switched out by a Trainer takes its Poison with it."""

    async def on_active_switched(self, ctx, player_id, outgoing, incoming,
                                 outgoing_conditions, via_trainer, carrier):
        if not via_trainer or POISONED not in outgoing_conditions:
            return
        await ctx.apply_special_condition(incoming, SpecialConditions.POISONED)


card = StadiumCardDef(
    guid="cf6a3667-cbcc-5ead-b1ec-1ad793af782e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DustIsland.Name",
    display_name="Dust Island",
    searchable_by=["Dust Island", "Stadium"],
    subtypes=["Stadium"],
    collector_number=168,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=DustIslandPassive(),
)
