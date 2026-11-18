from ptcgo.game.data_utils import ItemCardDef
from ptcgo.game.attributes import Rarities, AttrID, SpecialConditions, CLIENT_SPECIAL_CONDITION_NAMES
from ptcgo.game.card_effects.trainers import named
from ptcgo.game.card_effects.passives_common import Passive


_KOGA = named("Koga")


class KogaPoisonPassive(Passive):
    """This turn: an attack from a Pokemon with Koga in its name that damages
    the Defending Pokemon leaves it Poisoned."""

    async def attack_followup(self, ctx, carrier):
        attacker = getattr(ctx, "attacker", None)
        defender = ctx.opponent_active()
        if attacker is None or defender is None:
            return
        if attacker.owning_player_id != ctx.player_id or not _KOGA(attacker):
            return
        dealt = (getattr(ctx, "attack_damage", None) or {}).get(defender.entity_id)
        if not dealt or dealt[0] <= 0:
            return
        poisoned = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.POISONED]
        if poisoned in (defender.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return
        if defender not in ctx.opponent_pokemon_in_play():
            return
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)


async def _koga(ctx):
    """Ride a this-turn watcher on every in-play Pokemon of the effect owner;
    the next Koga attack that connects poisons what it hit."""
    expires = ctx.session.turn_state.turn_number
    for pokemon in ctx.my_pokemon_in_play():
        ctx.add_temporary_passive(pokemon, KogaPoisonPassive(),
                                  expires_after_turn=expires)


card = ItemCardDef(
    guid="57d8742f-c836-583f-8d37-3fea4e074b1b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Koga.Name",
    display_name="Koga",
    searchable_by=["Koga"],
    subtypes=[],
    collector_number=19,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    effect=_koga,
)
