from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.attributes import SpecialConditions


async def diamond_dust(ctx):
    """Printed 20, then on heads the Defending Pokemon is Paralyzed and every
    Benched Pokemon of theirs takes 10 (no Weakness or Resistance)."""
    await ctx.deal_damage()
    heads = await ctx.flip_coins(1, "Diamond Dust")
    if not heads or not heads[0]:
        return
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    for pokemon in list(ctx.opponent_bench()):
        await ctx.deal_damage(10, target=pokemon, apply_modifiers=False)

card = PokemonCardDef(
    guid="dc4b72a1-f8f4-5a65-b2cd-e6fb9b3e30a3",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Attack(
            title="Diamond Dust",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and this attack does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=20,
            effect=diamond_dust,
        ),
    ],
)