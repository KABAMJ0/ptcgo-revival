from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.scheduling import TurnBoundary


async def _burning_scent(ctx):
    """Burning Scent: may Red Card the Defending spot, then Burn + Poison."""
    if await ctx.ask_yes_no(
            "Switch 1 of your opponent's Benched Pokemon with the Defending Pokemon?"):
        bench = ctx.opponent_bench()
        if bench:
            target = await ctx.choose_pokemon(bench, "Choose a Benched Pokemon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.apply_special_condition(defender, SpecialConditions.BURNED)
    await ctx.apply_special_condition(defender, SpecialConditions.POISONED)


async def _energy_dissolve(ctx):
    """Energy Dissolve: one of the Defending Pokemon's Energy goes at the end
    of the opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return

    async def _strip(later):
        energies = later.attached_energies(defender)
        if energies:
            await later.discard_cards(energies[:1])

    ctx.schedule_turn_effect(TurnBoundary.END_OF_OPPONENT_NEXT_TURN, _strip,
                            require_source_in_play=True)

card = PokemonCardDef(
    guid="c5490b45-8648-5662-b953-f7b27486f66e",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=44,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Burning Scent",
            game_text="The Defending Pok\u00e9mon is now Burned and Poisoned. Before applying these effects, you may switch 1 of the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Burned and Poisoned.",
            cost={},
            effect=_burning_scent,
        ),
        Attack(
            title="Energy Dissolve",
            game_text="Discard an Energy attached to the Defending Pok\u00e9mon at the end of your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=_energy_dissolve,
        ),
    ],
)