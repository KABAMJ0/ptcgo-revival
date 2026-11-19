from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type


async def flame_pillar(ctx):
    """Printed 30; you may discard a Fire Energy to then do 10 to a chosen
    Benched Pokemon (no Weakness or Resistance)."""
    await ctx.deal_damage()
    fire = [e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.FIRE.value)]
    bench = ctx.opponent_bench()
    if not fire or not bench:
        return
    if not await ctx.ask_yes_no("Discard a Fire Energy to hit a Benched Pokemon?"):
        return
    gone = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.FIRE.value),
        prompt="Discard a Fire Energy")
    if not gone:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
    if target is not None:
        await ctx.deal_damage(10, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="3ab8a9c6-2017-550f-9442-dbf43021fdb2",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkRapidash.Name",
    display_name="Dark Rapidash",
    searchable_by=["Dark Rapidash", "Stage 1", "DarkRapidash"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    family_id=77,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Flame Pillar",
            game_text="You may discard 1 Fire Energy card attached to Dark Rapidash when you use this attack. If you do and if your opponent has any Benched Pok\u00e9mon, choose 1 of them and this attack does 10 damage to it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            effect=flame_pillar,
        ),
    ],
)