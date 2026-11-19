from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

async def dark_bind(ctx):
    """You may discard a Darkness Energy from this Pokemon; if you do, the
    Defending Pokemon is now Paralyzed."""
    energies = [card for card in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(card, PokemonTypes.DARKNESS.value)]
    if not energies:
        return
    if not await ctx.ask_yes_no("Discard a Darkness Energy to Paralyze the Defending Pokemon?"):
        return
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1,
        predicate=lambda card: energy_provides_type(card, PokemonTypes.DARKNESS.value),
        prompt="Discard a Darkness Energy card")
    if discarded:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="1fb57766-4e66-53d8-ab73-2f2db6d17a5d",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCacturne.Name",
    display_name="Team Aqua's Cacturne",
    searchable_by=["Team Aqua's Cacturne", "Stage 1", "TeamAquasCacturne"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Dark Bind",
            game_text="You may discard a Darkness Energy card attached to Team Aqua's Cacturne. If you do, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=dark_bind,
        ),
        Attack(
            title="Poison Barb",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)