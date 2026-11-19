from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_all_attacks


async def _crushing_earth(ctx):
    results = await ctx.flip_coins(1, "Crushing Earth")
    if results and results[0]:
        await ctx.deal_damage()
        for pokemon in ctx.my_bench() + ctx.opponent_bench():
            await ctx.deal_damage(10, target=pokemon)
    if ctx.attacker is not None:
        lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="8eac7865-2846-57e5-bc80-439a1cf44d90",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningSteelix.Name",
    display_name="Shining Steelix",
    searchable_by=["Shining Steelix", "Basic", "ShiningSteelix"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=208,
    abilities=[
        Attack(
            title="Crushing Earth",
            game_text="Flip a coin. If heads, this attack does 10 damage to each Benched Pok\u00e9mon (yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, this attack does nothing. Either way, Shining Steelix can't attack during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.FIGHTING: 2},
            damage=80,
            effect=_crushing_earth,
        ),
    ],
)