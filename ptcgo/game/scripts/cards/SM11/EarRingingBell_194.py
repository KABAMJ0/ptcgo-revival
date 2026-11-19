from ptcgo.game.data_utils import PokemonToolCardDef, Ability, Triggers
from ptcgo.game.attributes import Rarities, SpecialConditions
from ptcgo.game.card_effects.pokemon import in_active_spot


async def ear_ringing_bell(ctx):
    """Holder in the Active Spot damaged by an opponent's attack (even if
    Knocked Out): the Attacking Pokemon is now Confused."""
    if not in_active_spot(ctx.board, ctx.player_id, ctx.source):
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.apply_special_condition(attacker, SpecialConditions.CONFUSED)


card = PokemonToolCardDef(
    guid="2d77f5bb-b373-5265-8b33-6902f10fffe8",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EarRingingBell.Name",
    display_name="Ear-Ringing Bell",
    searchable_by=["Ear-Ringing Bell", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=194,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Ear-Ringing Bell",
            game_text="If the Pok\u00e9mon this card is attached to is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if that Pok\u00e9mon is Knocked Out), the Attacking Pok\u00e9mon is now Confused.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=ear_ringing_bell,
        ),
    ],
)
