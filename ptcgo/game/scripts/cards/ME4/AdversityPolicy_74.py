from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import AttrID, Rarities
from ptcgo.game.session.passives import carrier_pokemon


async def _adversity_policy(ctx):
    attacker = ctx.damaged_by
    tool = ctx.ability_source
    if attacker is None or tool is None or attacker.owning_player_id == ctx.player_id:
        return
    holder = carrier_pokemon(tool)
    if holder is None or ctx.board.active_pokemon(ctx.player_id) is not holder:
        return
    weakness = holder.get_attribute(AttrID.WEAKNESS_TYPES) or []
    if not set(weakness) & set(attacker.get_attribute(AttrID.POKEMON_TYPES) or []):
        return
    await ctx.draw_cards(3)


card = PokemonToolCardDef(
    guid="b2d1d8e8-308a-59cd-a63a-1cf37fc28c6f",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdversityPolicy.Name",
    display_name="Adversity Policy",
    searchable_by=["Adversity Policy", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=74,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    granted_abilities=[Ability(
        title="Adversity Policy",
        trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        effect=_adversity_policy,
    )],
)
