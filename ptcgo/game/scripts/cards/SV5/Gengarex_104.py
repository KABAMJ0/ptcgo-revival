from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Triggers


async def biting_whirlpool(ctx):
    """Whenever your opponent attaches an Energy card from their hand to 1 of
    their Pokémon, put 2 damage counters on that Pokémon."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    await ctx.deal_damage(20, target=receiver, apply_modifiers=False, as_counters=True)


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
    guid="ab8d2803-e3dd-5fad-8884-44fecd1308bf",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengarex.Name",
    display_name="Gengar ex",
    searchable_by=["Gengar ex", "Stage 2", "ex", "Gengarex"],
    subtypes=["Stage 2", "ex"],
    collector_number=104,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Gnawing Curse",
            game_text="Whenever your opponent attaches an Energy card from their hand to 1 of their Pok\u00e9mon, put 2 damage counters on that Pok\u00e9mon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=biting_whirlpool,
        ),
        Attack(
            title="Tricky Steps",
            game_text="You may move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=160,
            effect=_tricky_steps,
        ),
    ],
)