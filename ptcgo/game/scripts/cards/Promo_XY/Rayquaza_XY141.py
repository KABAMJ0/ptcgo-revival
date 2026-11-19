from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def dragon_blast(ctx):
    """Printed damage, then discard a Fire Energy and a Lightning Energy."""
    from ptcgo.game.card_effects.pokemon import energy_provides_type
    await ctx.deal_damage()
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=lambda c: energy_provides_type(c, PokemonTypes.FIRE.value),
        prompt="Choose a Fire Energy to discard")
    await ctx.discard_energy_from(
        ctx.attacker, 1, predicate=lambda c: energy_provides_type(c, PokemonTypes.LIGHTNING.value),
        prompt="Choose a Lightning Energy to discard")


card = PokemonCardDef(
    guid="8e10320d-08f4-5ccd-a0cc-99ebffb7694c",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rayquaza.Name",
    display_name="Rayquaza",
    searchable_by=["Rayquaza", "Basic", "Rayquaza"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=384,
    abilities=[
        Attack(
            title="Dual Claw",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
        Attack(
            title="Dragon Blast",
            game_text="Discard 1 Fire Energy and 1 Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=dragon_blast,
        ),
    ],
)