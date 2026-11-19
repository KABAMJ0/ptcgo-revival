from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage


async def glance(ctx):
    """Look at the top card of your opponent's deck."""
    top = ctx.deck_top(1, player_id=ctx.opponent_id)
    if not top:
        return
    await ctx.present_card_choice(
        top[0], "Top card of your opponent's deck", ["OK"])

card = PokemonCardDef(
    guid="1fdb2c25-8613-522c-935d-a006aa3bf46f",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic", "Minccino"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Glance",
            game_text="Look at the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=glance,
        ),
        Attack(
            title="Tail Slap",
            game_text="Flip 2 coins. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)