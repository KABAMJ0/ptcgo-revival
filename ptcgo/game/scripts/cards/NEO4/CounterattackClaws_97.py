from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot


async def _counterattack_claws(ctx):
    """The Active holder was damaged by an opponent's attack: heads puts 2
    damage counters on the Attacking Pokemon, then the tool is discarded."""
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == ctx.player_id:
        return
    if not is_in_active_spot(ctx.source):
        return
    if (await ctx.flip_coins(1, title="Counterattack Claws"))[0]:
        await ctx.deal_damage(20, target=attacker, apply_modifiers=False,
                              as_counters=True)
    tool = ctx.ability_source
    if tool is not None:
        await ctx.discard_cards([tool])


card = PokemonToolCardDef(
    guid="7dd63a07-5714-5b3d-9cab-c7c9b3519ece",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterattackClaws.Name",
    display_name="Counterattack Claws",
    searchable_by=["Counterattack Claws", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Counterattack Claws",
            game_text="During your opponent's turn, if the Pokemon this card is attached to is your Active Pokemon and an opponent's attack damages it (even if it is Knocked Out), flip a coin. If heads, put 2 damage counters on the Defending Pokemon. Then, discard Counterattack Claws.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_counterattack_claws,
        ),
    ],
)
