from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions


async def _ice_fang(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Ice Fang")
    if not (results and results[0]):
        return
    defender = ctx.defender
    if defender is None:
        return
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    if not ctx.effects_blocked(defender):
        await ctx.discard_energy_from(
            defender, 1, prompt="Discard an Energy card from the Defending Pok\u00e9mon")


async def _charge_through(ctx):
    await ctx.deal_damage()
    if not await ctx.ask_yes_no(
            "Do 40 more damage and 40 damage to 1 of your opponent's Benched "
            "Pok\u00e9mon? If you do, Mamoswine does 40 damage to itself."):
        return
    await ctx.deal_damage(40)
    bench = ctx.opponent_bench()
    if bench:
        picks = await ctx.choose_cards(
            bench, 1, prompt="Choose a Benched Pok\u00e9mon to take 40 damage")
        for pokemon in picks:
            await ctx.deal_damage(40, target=pokemon)
    if ctx.attacker is not None:
        await ctx.deal_damage(40, target=ctx.attacker, apply_modifiers=False)


card = PokemonCardDef(
    guid="c4978f70-2084-5594-8ee9-0fce52d8db5b",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name",
    display_name="Mamoswine",
    searchable_by=["Mamoswine", "Stage 2", "Mamoswine"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Attack(
            title="Ice Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=_ice_fang,
        ),
        Attack(
            title="Charge Through",
            game_text="You may do 60 damage plus 40 more damage and 40 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If you do, Mamoswine does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=_charge_through,
        ),
    ],
)