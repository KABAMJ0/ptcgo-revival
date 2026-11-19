from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _firefighting(ctx):
    """Discard a Fire Energy attached to the Defending Pokemon."""
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, 1,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.FIRE.value),
        prompt="Choose a Fire Energy to discard")


card = PokemonCardDef(
    guid="b6e34221-da09-5b1d-87ef-6891ab236b10",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Firefighting",
            game_text="Discard a Fire Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=_firefighting,
        ),
    ],
)