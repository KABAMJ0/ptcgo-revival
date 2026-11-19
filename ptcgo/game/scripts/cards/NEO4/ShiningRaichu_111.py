from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy


async def _thundersquall(ctx):
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Benched Pok\u00e9mon to take damage")
    water = count_energy(scope="self", energy_type=PokemonTypes.WATER)(ctx)
    if target is not None and water:
        await ctx.deal_damage(10 * water, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="40a27a7a-bd70-56ce-b583-9ebd34ee2476",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningRaichu.Name",
    display_name="Shining Raichu",
    searchable_by=["Shining Raichu", "Basic", "ShiningRaichu"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=26,
    abilities=[
        Attack(
            title="Thundersquall",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to that Pok\u00e9mon for each Water Energy attached to Shining Raichu. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.WATER: 2},
            damage=40,
            effect=_thundersquall,
        ),
    ],
)