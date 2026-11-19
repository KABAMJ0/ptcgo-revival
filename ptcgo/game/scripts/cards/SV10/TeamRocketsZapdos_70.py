from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _tricky_steps(ctx):
    await ctx.deal_damage()
    active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if active is None or not bench or ctx.effects_blocked(active):
        return
    energies = ctx.attached_energies(active)
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon?"
    ):
        return
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not picked:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the Benched Pokémon to move the Energy to"
    )
    if target is not None:
        await ctx.move_energy(picked[0], target)


card = PokemonCardDef(
    guid="f6e88f06-60ae-5a5f-9dfb-44ac3c3e0eea",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsZapdos.Name",
    display_name="Team Rocket's Zapdos",
    searchable_by=["Team Rocket's Zapdos", "Basic", "TeamRocketsZapdos"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Jamming Wing",
            game_text="You may move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_tricky_steps,
        ),
        Attack(
            title="Wicked Thunder",
            game_text="If this Pok\u00e9mon has any Team Rocket's Energy attached, this attack does 60 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)