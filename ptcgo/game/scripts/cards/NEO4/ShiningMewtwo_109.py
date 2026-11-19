from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon
from ptcgo.game.card_effects.pokemon import energy_provides_type


class _ReflectShield(Passive):
    """Flip to blank an attack hit on Shining Mewtwo and burn the attacker."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if carrier_pokemon(carrier) is not target:
            return None
        results = await ctx.flip_coins(1, "Reflect Shield")
        if not (results and results[0]):
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(20, target=attacker, apply_modifiers=False)
        return 0


async def _reflect_shield(ctx):
    if ctx.attacker is not None:
        ctx.add_passive_through_opponents_turn(ctx.attacker, _ReflectShield())


async def _psyburst(ctx):
    attacker = ctx.attacker
    if attacker is None:
        return
    fire = [energy for energy in ctx.attached_energies(attacker)
            if energy_provides_type(energy, PokemonTypes.FIRE.value)]
    if not fire:
        return  # "or this attack does nothing"
    await ctx.discard_cards([fire[0]])
    defender = ctx.defender
    extra = len(ctx.attached_energies(defender)) if defender is not None else 0
    await ctx.deal_damage(40 + 10 * extra)


card = PokemonCardDef(
    guid="12f4704d-272a-5fe1-9d6e-c42b0326f141",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningMewtwo.Name",
    display_name="Shining Mewtwo",
    searchable_by=["Shining Mewtwo", "Basic", "ShiningMewtwo"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Reflect Shield",
            game_text="If an attack does damage to Shining Mewtwo during your opponent's next turn (even if Shining Mewtwo is Knocked Out), flip a coin. If heads, prevent all damage done to Shining Mewtwo from that attack (any other effects of attacks still happen) and do 20 damage to the attacking Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.LIGHTNING: 1},
            effect=_reflect_shield,
        ),
        Attack(
            title="Psyburst",
            game_text="Discard a Fire Energy card attached to Shining Mewtwo or this attack does nothing. This attack does 40 damage plus 10 damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=_psyburst,
        ),
    ],
)