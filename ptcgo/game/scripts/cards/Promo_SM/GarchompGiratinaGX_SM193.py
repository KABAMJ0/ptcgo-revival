from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, damage_counters_on, snipe_attack

async def gg_end(ctx):
    """Discard 1 of the opponent's Pokemon and everything on it; with at least
    3 extra Fighting Energy, discard 2 more of their Pokemon the same way."""
    from ptcgo.game.card_effects.attacks_common import extra_energy_attached
    count = 1 + (2 if extra_energy_attached(3, PokemonTypes.FIGHTING.value)(ctx) else 0)
    pool = [p for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)]
    if not pool:
        return
    for _ in range(min(count, len(pool))):
        target = await ctx.choose_pokemon(pool, "Choose a Pokemon to discard")
        if target is None:
            return
        pool.remove(target)
        await ctx.discard_cards([target] + list(getattr(target, "children", None) or []))


card = PokemonCardDef(
    guid="3f656f8b-9821-5a61-82d7-d331cf032f8c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompGiratinaGX.Name",
    display_name="Garchomp & Giratina-GX",
    searchable_by=["Garchomp & Giratina-GX", "Basic", "TAG TEAM", "GX", "GarchompGiratinaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=193,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(40, pool="any", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Calamitous Slash",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            effect=bonus_if(lambda ctx: damage_counters_on("defender")(ctx) > 0, 80),
        ),
        Attack(
            title="GG End-GX",
            game_text="Discard 1 of your opponent's Pok\u00e9mon and all cards attached to it. If this Pok\u00e9mon has at least 3 extra Fighting Energy attached to it (in addition to this attack's cost), discard 2 of your opponent's Pok\u00e9mon instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIGHTING: 1},
            effect=gg_end,
        ),
    ],
)