from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def poison_ring(ctx):
    """The Defending Pokemon is Poisoned and cannot retreat through your
    opponent's next turn."""
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        ctx.lock_retreat(ctx.defender, ctx.session.turn_state.turn_number + 1)

card = PokemonCardDef(
    guid="526c02fb-ae40-5e91-90d6-a111f93c9819",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sceptileex.Name",
    display_name="Sceptile ex",
    searchable_by=["Sceptile ex", "Stage 2", "ex", "Sceptileex"],
    subtypes=["Stage 2", "ex"],
    collector_number=93,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name",
    family_id=254,
    abilities=[
        Attack(
            title="Green Heal",
            game_text="Remove 4 damage counters from each of your Pok\u00e9mon that has Grass Energy attached. If that Pok\u00e9mon has less than 4 damage counters, remove all of them.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Poison Ring",
            game_text="The Defending Pok\u00e9mon is now Poisoned. The Defending Pok\u00e9mon can't retreat until the end of your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=poison_ring,
        ),
        Attack(
            title="Slashing Strike",
            game_text="Sceptile ex can't use Slashing Strike during your next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)