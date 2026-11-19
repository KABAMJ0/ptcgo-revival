from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def bubble_shoot(ctx):
    """20 damage per Water Energy attached to Corsola, to 1 of the opponent's
    Pokemon (no Weakness or Resistance when it lands on the Bench)."""
    water = sum(1 for energy in ctx.attached_energies(ctx.attacker)
                if energy_provides_type(energy, PokemonTypes.WATER.value))
    if water <= 0:
        return
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokemon")
    if target is not None:
        await ctx.deal_damage(20 * water, target=target)

card = PokemonCardDef(
    guid="4f607db8-8ba0-54ac-b265-bfa64688debe",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="DM",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Bubble Shoot",
            game_text="This attack does 20 damage times the amount of Water Energy attached to this Pok\u00e9mon to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=bubble_shoot,
        ),
    ],
)