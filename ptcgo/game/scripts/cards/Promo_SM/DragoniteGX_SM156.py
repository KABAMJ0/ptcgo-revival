from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.session.constants import BENCH_CAPACITY

async def _bench_from_discard(ctx, predicate, count, label):
    """Put up to `count` matching cards from your discard pile onto your Bench."""
    space = max(0, len(ctx.my_bench()))
    room = BENCH_CAPACITY - space
    pool = [c for c in ctx.discard_pile(ctx.player_id) if predicate(c)]
    if room <= 0 or not pool:
        return
    for _ in range(min(count, room)):
        if not pool:
            break
        picks = await ctx.choose_cards(pool, 1, minimum=1,
                                       prompt=f"Choose {label} to put onto your Bench")
        if not picks:
            break
        pool.remove(picks[0])
        await ctx.bench_pokemon(picks[0])

async def dragonporter(ctx):
    """Put up to 3 Dragon Pokemon from the discard pile onto your Bench."""
    def is_dragon(card):
        return PokemonTypes.DRAGON.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])
    await _bench_from_discard(ctx, is_dragon, 3, "Dragon Pokemon")


card = PokemonCardDef(
    guid="3cd923f5-73c1-57db-869e-e52c094162ef",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteGX.Name",
    display_name="Dragonite-GX",
    searchable_by=["Dragonite-GX", "Stage 2", "GX", "DragoniteGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=156,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=149,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=lock_self_attack(),
        ),
        Attack(
            title="Dragonporter-GX",
            game_text="Put 3 Dragon Pok\u00e9mon from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=dragonporter,
        ),
    ],
)