from ptcgo.game.card_effects.attacks_common import flip_damage, ignore_modifier_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _bullet_uppercut(ctx):
    """Printed 10, +60 against a GX or EX; the damage ignores effects on the
    opponent's Active."""
    from ptcgo.game.card_effects.pokemon import is_pokemon_gx, is_pokemon_EX
    target = ctx.defender
    is_gx = target is not None and (is_pokemon_gx(target.archetype_id)
                                    or is_pokemon_EX(target.archetype_id))
    bonus = 60 if is_gx else 0
    await ctx.deal_damage(10 + bonus, ignore_target_effects=True)


card = PokemonCardDef(
    guid="48930db6-53ac-50f4-a169-0e798737cd29",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZekromGX.Name",
    display_name="Zekrom-GX",
    searchable_by=["Zekrom-GX", "Basic", "GX", "ZekromGX"],
    subtypes=["Basic", "GX"],
    collector_number=138,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=644,
    abilities=[
        Attack(
            title="Bullet Uppercut",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-GX or a Pok\u00e9mon-EX, this attack does 60 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=ignore_modifier_attack(ignore_target_effects=True, damage=None) if False else _bullet_uppercut,
        ),
        Attack(
            title="Swift Bolt Strike",
            game_text="Flip 2 coins. This attack does 60 more damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=60),
        ),
        Attack(
            title="Rampage Bolt-GX",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)