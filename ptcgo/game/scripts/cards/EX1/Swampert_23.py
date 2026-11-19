from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def natural_remedy(ctx):
    """When you attach a Water Energy from your hand to Swampert, remove 1
    damage counter from it."""
    energy = getattr(ctx, "attached_energy", None)
    receiver = getattr(ctx, "energy_receiver", None)
    if ctx.source is None or receiver is not ctx.source or energy is None:
        return
    if not energy_provides_type(energy, PokemonTypes.WATER.value):
        return
    await ctx.heal(10, ctx.source)

card = PokemonCardDef(
    guid="6fda4bd1-c99d-5e65-b5d8-992f08534542",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="EX1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Natural Remedy",
            game_text="Once during your turn (before your attack), when you attach a Water Energy card from your hand to Swampert, remove 1 damage counter from Swampert.",
            effect=natural_remedy,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        ),
        Attack(
            title="Water Arrow",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=snipe_attack(20, pool="any"),
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)