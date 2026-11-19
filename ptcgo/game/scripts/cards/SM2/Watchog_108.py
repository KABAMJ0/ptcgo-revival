from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

async def _scrutinize(ctx):
    top_cards = ctx.deck_top(2, ctx.opponent_id)
    if not top_cards:
        return
    if len(top_cards) == 1:
        picks = top_cards
    else:
        await ctx.reveal_cards(top_cards, to_player=ctx.player_id)
        picks = await ctx.choose_cards(
            top_cards, 1, minimum=1,
            prompt="Choose a card to discard from the top of their deck")
    await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="a5efd131-a663-598b-8718-c970f267e327",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    display_name="Watchog",
    searchable_by=["Watchog", "Stage 1", "Watchog"],
    subtypes=["Stage 1"],
    collector_number=108,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=504,
    abilities=[
        Attack(
            title="Scrutinize",
            game_text="Look at the top 2 cards of your opponent's deck, discard 1 of them, and put the other card back.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_scrutinize,
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=60),
        ),
    ],
)