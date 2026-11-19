from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _magnetic_lines(ctx):
    """Printed damage, then you may move an Energy off the Defending Pokemon
    onto one of your opponent's Benched Pokemon."""
    await ctx.deal_damage()
    defender = ctx.defender
    bench = ctx.opponent_bench()
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = list(ctx.attached_energies(defender))
    if not energies:
        return
    picked = energies if len(energies) == 1 else await ctx.choose_cards(
        energies, 1, minimum=0,
        prompt="Choose an Energy to move to a Benched Pok\u00e9mon")
    if not picked:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pok\u00e9mon to move the Energy to",
        optional=True)
    if target is None:
        return
    await ctx.move_energy(picked[0], target)


card = PokemonCardDef(
    guid="51e76940-9988-5bae-91f3-55d619a2925b",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1", "Probopass"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Magnetic Lines",
            game_text="You may move an Energy attached to the Defending Pok\u00e9mon to 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_magnetic_lines,
        ),
        Attack(
            title="Heavy Nose",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 30 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)