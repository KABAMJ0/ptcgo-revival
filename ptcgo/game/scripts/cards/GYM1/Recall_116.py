from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.session.passives import Passive, previous_evolution_attacks


class RecallGrantPassive(Passive):
    """The Active Pokemon may use the attacks of its Basic and Evolution cards."""

    def granted_attacks(self, board, pokemon, carrier):
        return previous_evolution_attacks(pokemon)


async def recall(ctx):
    """For your attack this turn, your Active Pokemon may use any attack from
    its Basic Pokemon card or any Evolution card attached to it."""
    active = ctx.my_active()
    if active is None:
        return
    ctx.add_temporary_passive(active, RecallGrantPassive(),
                              ctx.session.turn_state.turn_number)


card = ItemCardDef(
    guid="21b819d6-ad55-5873-a6e9-e9ffcc3a01b0",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recall.Name",
    display_name="Recall",
    searchable_by=["Recall"],
    subtypes=[],
    collector_number=116,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    effect=recall
)
