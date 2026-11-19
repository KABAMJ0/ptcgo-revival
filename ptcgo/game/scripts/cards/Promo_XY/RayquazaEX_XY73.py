from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def dragon_strike(ctx):
    """Printed 130; on tails this attack is locked through the user's next turn."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Dragon Strike")
    ability = ctx.ability
    if results and not results[0] and ctx.attacker is not None and ability.ability_id:
        ctx.session.turn_state.lock_attack(ctx.attacker.entity_id, ability.ability_id)


card = PokemonCardDef(
    guid="7ef20a18-10af-5589-92ea-9958520d6486",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    display_name="Rayquaza-EX",
    searchable_by=["Rayquaza-EX", "Basic", "EX", "RayquazaEX"],
    subtypes=["Basic", "EX"],
    collector_number=73,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Dragon Strike",
            game_text="Flip a coin. If tails, this Pok\u00e9mon can't use Dragon Strike during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=dragon_strike,
        ),
    ],
)