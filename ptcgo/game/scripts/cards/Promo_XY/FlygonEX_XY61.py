from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.card_effects.pokemon import in_active_spot

async def voice_of_the_sands(ctx):
    """The opponent picks one of their Benched Pokemon to become Active."""
    bench = [p for p in ctx.opponent_bench()]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose the opponent's new Active Pokemon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="3cb3be79-f760-5a31-9e7e-13be78899fcf",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlygonEX.Name",
    display_name="Flygon-EX",
    searchable_by=["Flygon-EX", "Basic", "EX", "FlygonEX"],
    subtypes=["Basic", "EX"],
    collector_number=61,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=330,
    abilities=[
        Ability(
            title="Voice of the Sands",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=in_active_spot,
            effect=voice_of_the_sands,
        ),
        Attack(
            title="Spiral Buzz",
            game_text="Flip a coin until you get tails. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=30),
        ),
    ],
)