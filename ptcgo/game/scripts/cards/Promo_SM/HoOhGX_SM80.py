from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.session.constants import BENCH_CAPACITY
from ptcgo.game.attributes import AttrID

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

async def eternal_light(ctx):
    """Put 3 in any combination of Fire Pokemon-GX and Fire Pokemon-EX from the
    discard pile onto your Bench."""
    from ptcgo.game.card_effects.pokemon import is_pokemon_gx, is_pokemon_EX
    def fire_gx_or_ex(card):
        if PokemonTypes.FIRE.value not in (card.get_attribute(AttrID.POKEMON_TYPES) or []):
            return False
        return is_pokemon_gx(card.archetype_id) or is_pokemon_EX(card.archetype_id)
    await _bench_from_discard(ctx, fire_gx_or_ex, 3, "Fire Pokemon-GX or Pokemon-EX")


card = PokemonCardDef(
    guid="3c1290a7-11d7-50cd-807f-c5f42d71e783",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhGX.Name",
    display_name="Ho-Oh-GX",
    searchable_by=["Ho-Oh-GX", "Basic", "GX", "HoOhGX"],
    subtypes=["Basic", "GX"],
    collector_number=80,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=250,
    abilities=[
        Attack(
            title="Sacred Fire",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(50, pool="any", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Phoenix Burn",
            game_text="This Pok\u00e9mon can't use Phoenix Burn during your next turn.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
        Attack(
            title="Eternal Light-GX",
            game_text="Put 3 in any combination of Fire Pok\u00e9mon-GX or Fire Pok\u00e9mon-EX from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=eternal_light,
        ),
    ],
)