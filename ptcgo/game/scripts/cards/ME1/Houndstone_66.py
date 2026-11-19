import random

from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def horrifying_bite(ctx):
    """30; flip until tails, then shuffle that many random cards of the
    opponent's hand into their deck."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails("Horrifying Bite")
    hand = ctx.hand(ctx.opponent_id)
    if heads <= 0 or not hand:
        return
    picks = random.sample(hand, min(heads, len(hand)))
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="56a631f7-67e8-5dc3-987c-74dcb0ec232c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1", "Houndstone"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Horrifying Bite",
            game_text="Flip a coin until you get tails. For each heads, choose a random card from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=horrifying_bite,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)