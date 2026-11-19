from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_basic_water_energy
from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.pokemon import is_water_energy


async def _drizzle(ctx):
    """Drizzle: up to 2 basic Water Energy from hand onto 1 Pokemon."""
    await attach_from_hand(predicate=is_basic_water_energy, count=2,
                           target="choice", minimum=0,
                           prompt="Choose up to 2 basic Water Energy cards")(ctx)


async def _high_tide(ctx):
    """High Tide: discard 2 Water Energy, then 20 to each Benched Pokemon."""
    await ctx.discard_energy_from(ctx.attacker, 2, predicate=is_water_energy,
                                  prompt="Discard 2 Water Energy")
    await ctx.deal_damage()
    for target in ctx.opponent_bench():
        await ctx.deal_damage(20, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="46403c79-6dae-5bfd-afc7-46306ff2d796",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Drizzle",
            game_text="Choose up to 2 basic Water Energy cards from your hand and attach them to 1 of your Pok\u00e9mon.",
            cost={},
            effect=_drizzle,
        ),
        Attack(
            title="High Tide",
            game_text="Discard 2 Water Energy attached to Kyogre. This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=_high_tide,
        ),
    ],
)