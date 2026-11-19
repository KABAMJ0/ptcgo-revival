from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def clamp_crush(ctx):
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Clamp Crush")
    if not heads or not heads[0]:
        return
    defender = ctx.defender
    if defender is None:
        return
    await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)
    await ctx.discard_energy_from(
        defender, 1, prompt="Discard an Energy attached to that Pokemon")

card = PokemonCardDef(
    guid="8d609f12-e008-58ab-8afb-86682088acab",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cloyster.Name",
    display_name="Cloyster",
    searchable_by=["Cloyster", "Stage 1", "Cloyster"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
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
            effect=clamp_crush,
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