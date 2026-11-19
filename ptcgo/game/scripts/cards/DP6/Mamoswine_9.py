from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _charge_through(ctx):
    """Charge Through: the whole 60+40 and the Bench hit are one yes/no; the
    recoil rides the same bargain (declined = the attack does nothing)."""
    if not await ctx.ask_yes_no(
            "Do 60 damage plus 40 more damage and 40 damage to 1 of your "
            "opponent's Benched Pokemon? If you do, Mamoswine does 40 damage "
            "to itself."):
        return
    await ctx.deal_damage(100)
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
        if target is not None:
            await ctx.deal_damage(40, target=target, apply_modifiers=False)
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
            effect=unimplemented,
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