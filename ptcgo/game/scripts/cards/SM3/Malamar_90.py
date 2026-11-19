from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack


async def energy_slosh(ctx):
    """Printed 70; you may move every Energy on this Pokemon onto 1 of your
    Benched Pokemon."""
    await ctx.deal_damage()
    attacker = ctx.attacker
    bench = ctx.my_bench()
    energies = list(ctx.attached_energies(attacker)) if attacker is not None else []
    if not bench or not energies:
        return
    if not await ctx.ask_yes_no(
            "Move all Energy attached to this Pokémon to 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move all Energy to")
    if target is None:
        return
    for energy in energies:
        await ctx.move_energy(energy, target)


card = PokemonCardDef(
    guid="4328d7ba-97a8-5088-94ae-602c6ae9a038",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Malamar.Name",
    display_name="Malamar",
    searchable_by=["Malamar", "Stage 1", "Malamar"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SM3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name",
    family_id=686,
    abilities=[
        Attack(
            title="Psybeam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Energy Slosh",
            game_text="You may move all Energy attached to this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=energy_slosh,
        ),
    ],
)