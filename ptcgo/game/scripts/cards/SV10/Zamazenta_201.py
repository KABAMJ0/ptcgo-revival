from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import RetaliateCountersPassive, carrier_pokemon


class DamageTakenCounters(RetaliateCountersPassive):
    """Counters equal to the damage taken, not a fixed count."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount >= 10):
            return None
        if target is not carrier_pokemon(carrier):
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


async def strong_bash(ctx):
    """70 damage; during the opponent's next turn, whoever damages this
    Pokemon takes counters equal to the damage it dealt."""
    await ctx.deal_damage()
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(
            ctx.attacker, DamageTakenCounters())


card = PokemonCardDef(
    guid="1cca1b68-8681-5973-bc51-92f3e5d50004",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zamazenta.Name",
    display_name="Zamazenta",
    searchable_by=["Zamazenta", "Basic", "Zamazenta"],
    subtypes=["Basic"],
    collector_number=201,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=889,
    abilities=[
        Attack(
            title="Strong Bash",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=strong_bash,
        ),
    ],
)