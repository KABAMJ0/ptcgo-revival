from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _energy_kick(ctx):
    results = await ctx.flip_coins(1, "Energy Kick")
    if not (results and results[0]):
        return
    defender = ctx.defender
    bench = ctx.opponent_bench()
    if defender is None or not bench:
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    energy = energies[0]
    if len(energies) > 1:
        picked = await ctx.choose_cards(
            energies, 1,
            prompt="Choose an Energy card attached to the Defending Pokémon")
        if not picked:
            return
        energy = picked[0]
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose a Pokémon to move the Energy to")
    if target is not None:
        await ctx.move_energy(energy, target)


card = PokemonCardDef(
    guid="bda34a9e-e50d-5194-abd9-7dd6b864794d",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elekid.Name",
    display_name="Elekid",
    searchable_by=["Elekid", "Baby", "Elekid"],
    subtypes=["Baby"],
    collector_number=9,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=239,
    abilities=[
        Attack(
            title="Energy Kick",
            game_text="Flip a coin. If heads, choose an Energy card attached to the Defending Pok\u00e9mon. Your opponent moves that card to 1 of his or her other Pok\u00e9mon. (If your opponent has no Benched Pok\u00e9mon, this attack does nothing.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_energy_kick,
        ),
    ],
)