from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_fire(card) -> bool:
    return energy_provides_type(card, PokemonTypes.FIRE.value)


async def _scorching_lava(ctx):
    discarded = await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=_is_fire, minimum=1,
        prompt="Choose a Fire Energy to discard from Slugma")
    if not discarded:
        return
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)

card = PokemonCardDef(
    guid="d700ffb7-0af2-5166-a4b7-99aeb02a7f5e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Scorching Lava",
            game_text="Discard a Fire Energy card attached to Slugma in order to use this attack. The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=_scorching_lava,
        ),
    ],
)
