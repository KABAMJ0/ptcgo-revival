from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.card_effects.attacks_common import place_counters, count_bench
from ptcgo.game.card_effects.support_common import requires_bench_space

async def netherworld_gate(ctx):
    """Once per turn, from the discard pile: you may put this Pokemon onto
    your Bench. If you do, put 3 damage counters on it."""
    if not await ctx.ask_yes_no("Put this Pokémon onto your Bench?"):
        return
    if await ctx.bench_pokemon(ctx.source):
        await ctx.deal_damage(30, target=ctx.source, apply_modifiers=False,
                              as_counters=True)

card = PokemonCardDef(
    guid="4376f0d2-1964-584e-9dcb-831ff2287ccf",
    key="SWSH11TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SWSH11TG",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=94,
    abilities=[
        Ability(
            title="Netherworld Gate",
            game_text="Once during your turn, if this Pok\u00e9mon is in your discard pile, you may put it onto your Bench. If you do, put 3 damage counters on this Pok\u00e9mon.",
            effect=netherworld_gate,
            condition=requires_bench_space(1),
        ),
        Attack(
            title="Screaming Circle",
            game_text="Put 2 damage counters on your opponent's Active Pok\u00e9mon for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(
                lambda ctx: 2 * count_bench("opponent")(ctx), "opponent_active"
            ),
        ),
    ],
)