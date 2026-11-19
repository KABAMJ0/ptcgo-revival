from ptcgo.game.data_utils import StadiumCardDef, unimplemented
from ptcgo.game.data_utils import Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.attributes import AttrID


def active_is_damaged(board, player_id, stadium) -> bool:
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    return (active.get_attribute(AttrID.HP, 0)
            < getattr(active, "attribute_originals", {}).get(AttrID.HP.value, 999))

async def healing_field(ctx):
    """Flip a coin. If heads, remove 2 damage counters from your Active
    Pokemon (1 if it only has 1)."""
    results = await ctx.flip_coins(1, "Healing Field")
    if not (results and all(results)):
        return
    active = ctx.my_active()
    if active is not None:
        await ctx.heal(20, active)


card = StadiumCardDef(
    guid="88ffd2cc-7c5b-5ddd-80f7-0edc1d5b9370",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingField.Name",
    display_name="Healing Field",
    searchable_by=["Healing Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Healing Field",
        activation=Activations.ONCE_PER_TURN,
            condition=active_is_damaged,
        effect=healing_field,
    )
)
