from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.pokemon import is_pokemon_EX, is_pokemon_gx


def _fire_gx_or_ex(card) -> bool:
    """A Fire Pokemon-GX or Pokemon-EX (the BW/XY spelling) in the discard."""
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types \
        and (is_pokemon_gx(card) or is_pokemon_EX(card))


async def eternal_flame_gx(ctx):
    """Put up to 3 Fire Pokemon-GX/EX from the discard pile onto your Bench,
    in any combination."""
    pool = [card for card in ctx.discard_pile(ctx.player_id)
            if _fire_gx_or_ex(card)]
    free = ctx.bench_limit() - len(ctx.my_bench())
    if not pool or free <= 0:
        return
    picks = await ctx.choose_cards(
        pool, min(3, free), minimum=0,
        prompt="Choose Fire Pokémon-GX or Pokémon-EX to put onto your Bench")
    for card in picks:
        await ctx.bench_pokemon(card)


card = PokemonCardDef(
    guid="a40c002a-290f-5084-bdf5-5247579b3c18",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoOhGX.Name",
    display_name="Ho-Oh-GX",
    searchable_by=["Ho-Oh-GX", "Basic", "GX", "HoOhGX"],
    subtypes=["Basic", "GX"],
    collector_number=21,
    set_code="SM3",
    rarity=Rarities.RareHolo,
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
            title="Eternal Flame-GX",
            game_text="Put 3 in any combination of Fire Pok\u00e9mon-GX or Fire Pok\u00e9mon-EX from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=eternal_flame_gx,
        ),
    ],
)