from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def night_cyclone(ctx):
    """160 damage, then move all Energy from this Pokemon to your Benched Pokemon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = list(ctx.attached_energies(ctx.attacker))
    if not bench or not energies:
        return
    for energy in energies:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move this Energy to")
        if target is None:
            break
        await ctx.move_energy(energy, target)

card = PokemonCardDef(
    guid="786013ea-0537-5827-9c13-e0dc0529d001",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1", "Kilowattrel"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Storm Bolt",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=night_cyclone,
        ),
    ],
)