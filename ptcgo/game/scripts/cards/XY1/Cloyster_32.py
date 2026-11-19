from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _clamp_crush(ctx):
    """30 damage; on heads the Defending Pokemon is Paralyzed and loses an
    Energy."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    results = await ctx.flip_coins(1, "Clamp Crush")
    if results and results[0]:
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
        await ctx.discard_energy_from(defender, 1)


card = PokemonCardDef(
    guid="1311e61f-4974-5f9b-b166-9776748d90c7",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster",
    searchable_by=["Cloyster", "Stage 1", "Cloyster"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellder.Name",
    family_id=90,
    abilities=[
        Attack(
            title="Clamp Crush",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed and discard an Energy attached to that Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_clamp_crush,
        ),
        Attack(
            title="Spike Cannon",
            game_text="Flip 5 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=5, per_heads=30),
        ),
    ],
)