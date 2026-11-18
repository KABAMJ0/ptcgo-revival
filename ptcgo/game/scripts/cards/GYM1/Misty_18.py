from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import requires_hand
from ptcgo.game.card_effects.trainers import named, with_discard_cost
from ptcgo.game.session.passives import TurnDamageModifier

async def _misty_boost(ctx):
    """This turn, an attack used by a Pokemon with Misty in its name does 20
    more damage to the Defending Pokemon."""
    ctx.add_turn_damage_modifier(
        TurnDamageModifier(20, ctx.player_id, source_predicate=named("Misty")))


card = ItemCardDef(
    guid="ef622217-068c-5818-9591-e1f69689b011",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=18,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    condition=requires_hand(n=2),
    effect=with_discard_cost(2, _misty_boost),
)
