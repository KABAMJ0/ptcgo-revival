from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def drag_off(ctx):
    target = None
    bench = ctx.opponent_bench()
    if bench and await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokémon with the Defending Pokémon?"):
        target = await ctx.choose_pokemon(bench, "Choose the new Defending Pokémon") or bench[0]
        await ctx.switch_active(ctx.opponent_id, target)
    await ctx.deal_damage(target=target)


card = PokemonCardDef(
    guid="f1009d9d-610b-50df-a011-73457eba2eaa",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may choose 1 of your opponent's Benched Pok\u00e9mon and switch it with the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=drag_off,
        ),
        Attack(
            title="Giga Hammer",
            game_text="Regigigas can't use Giga Hammer during your next turn.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=unimplemented,
        ),
    ],
)