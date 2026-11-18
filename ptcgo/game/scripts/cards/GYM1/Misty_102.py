from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.trainers import pokemon_named, with_discard_cost
from ptcgo.game.session.passives import TurnDamageModifier


async def _mistys_gift(ctx):
    ctx.add_turn_damage_modifier(TurnDamageModifier(
        amount=20, player_id=ctx.player_id,
        source_predicate=pokemon_named("misty")))


card = ItemCardDef(
    guid="95817130-6a28-598b-8901-6792f50d7d9f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Misty.Name",
    display_name="Misty",
    searchable_by=["Misty"],
    subtypes=[],
    collector_number=102,
    set_code="GYM1",
    rarity=Rarities.Rare,
    effect=with_discard_cost(2, _mistys_gift)
)
