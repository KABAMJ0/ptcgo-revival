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
    guid="77d987f2-91fa-5503-91fa-9a775a8522ff",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=386,
    abilities=[
        Attack(
            title="Psypunch",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
        Attack(
            title="Genome Spiral",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=night_cyclone,
        ),
    ],
)