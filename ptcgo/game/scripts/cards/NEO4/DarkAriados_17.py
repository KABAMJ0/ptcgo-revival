from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions


async def _entangle(ctx):
    """Entangle: pull their Benched Pokemon up, then heads Paralyzes it."""
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    heads = await ctx.flip_coins(1, "Entangle")
    if heads and all(heads):
        await ctx.apply_special_condition(defender, SpecialConditions.PARALYZED)


async def _poison_bind(ctx):
    """Poison Bind: Poisoned always; heads also nails it in place."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.apply_special_condition(defender, SpecialConditions.POISONED)
    heads = await ctx.flip_coins(1, "Poison Bind")
    if heads and all(heads):
        ctx.lock_retreat(defender)

card = PokemonCardDef(
    guid="abdda253-8ca1-515d-b14b-54854f12b240",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAriados.Name",
    display_name="Dark Ariados",
    searchable_by=["Dark Ariados", "Stage 1", "DarkAriados"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="NEO4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=168,
    abilities=[
        Attack(
            title="Entangle",
            game_text="If your opponent has any Benched Pok\u00e9mon, choose 1 of them and switch it with the Defending Pok\u00e9mon, then flip a coin. If heads, the new Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1},
            effect=_entangle,
        ),
        Attack(
            title="Poison Bind",
            game_text="The Defending Pok\u00e9mon is now Poisoned. Flip a coin. If heads, the Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn and if the effect of an attack, Pok\u00e9mon Power, or Trainer card would change that player's Active Pok\u00e9mon, that part of the effect does nothing.",
            cost={PokemonTypes.GRASS: 3},
            damage=30,
            effect=_poison_bind,
        ),
    ],
)