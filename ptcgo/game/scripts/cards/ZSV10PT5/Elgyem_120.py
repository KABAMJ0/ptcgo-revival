from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _slight_shift(ctx):
    theirs = ctx.opponent_pokemon_in_play()
    if len(theirs) < 2:
        return
    energies = [energy for pokemon in theirs
                for energy in ctx.attached_energies(pokemon)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy to move between their Pok\u00e9mon")
    if not picks:
        return
    await ctx.move_energy_freely(theirs, theirs, max_count=1,
                                 prompt="Choose where to move it")


async def _slight_shift_offered(ctx):
    theirs = ctx.opponent_pokemon_in_play()
    return len(theirs) >= 2 and any(ctx.attached_energies(p) for p in theirs)


card = PokemonCardDef(
    guid="897fb324-a15c-5d8a-91b1-c8489e4ccadf",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=605,
    abilities=[
        Attack(
            title="Slight Shift",
            game_text="Move an Energy from 1 of your opponent's Pok\u00e9mon to another of their Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_slight_shift,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)