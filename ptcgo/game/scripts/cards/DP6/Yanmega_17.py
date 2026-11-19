from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import opponent_switches
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.support_common import switch_self_attack


async def _sonic_wave(ctx):
    """Sonic Wave: printed damage, 10 to each of their Bench, then they switch."""
    await ctx.deal_damage()
    for target in ctx.opponent_bench():
        await ctx.deal_damage(10, target=target, apply_modifiers=False)
    await opponent_switches(ctx)


async def _pursue_and_turn(ctx):
    """Pursue and Turn: 60, or 80 plus a turn out when the defender is marked."""
    defender = ctx.defender
    marked = (defender is not None
              and defender.get_attribute(AttrID.HP, 0) <= ctx.max_hp(defender) - 20)
    await ctx.deal_damage(80 if marked else 60)
    if marked:
        await switch_self_attack(damage=0, optional=False)(ctx)


async def _pursue_and_turn(ctx):
    """Pursue and Turn: 60, or 80 plus a turn out when the defender is marked."""
    defender = ctx.defender
    marked = (defender is not None
              and defender.get_attribute(AttrID.HP, 0) <= ctx.max_hp(defender) - 20)
    await ctx.deal_damage(80 if marked else 60)
    if marked:
        await switch_self_attack(damage=0, optional=False)(ctx)

card = PokemonCardDef(
    guid="6a1fda79-6eb1-5329-a695-a31377a71cdc",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Yanmega"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Attack(
            title="Sonic Wave",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={},
            damage=10,
            effect=_sonic_wave,
        ),
        Attack(
            title="Pursue and Turn",
            game_text="If the Defending Pok\u00e9mon already has 2 or more damage counters on it, this attack does 60 damage plus 20 more damage and switch Yanmega with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=_pursue_and_turn,
        ),
    ],
)