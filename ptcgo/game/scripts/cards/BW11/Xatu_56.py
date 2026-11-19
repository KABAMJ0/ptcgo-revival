import random

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

_RPS = ["Rock", "Paper", "Scissors"]


async def fortunate_draw(ctx):
    """One round of Rock-Paper-Scissors: the winner draws 3 AND the loser
    discards the top 3 of their deck. The card prints no "until someone wins",
    so a tie leaves both players alone."""
    prompt = "Rock-Paper-Scissors: choose your play."
    mine = await ctx.choose(prompt, _RPS)
    # The opponent sees a shuffled order so an AI (auto-first-button) plays
    # randomly; the index is mapped back to the real play.
    order = random.sample(_RPS, 3)
    pick = await ctx.choose(prompt, order, player_id=ctx.opponent_id)
    theirs = _RPS.index(order[pick])
    if mine == theirs:
        return
    winner, loser = (ctx.player_id, ctx.opponent_id) \
        if (mine - theirs) % 3 == 1 else (ctx.opponent_id, ctx.player_id)
    await ctx.draw_cards(3, winner)
    await ctx.discard_cards(ctx.deck_top(3, player_id=loser))


card = PokemonCardDef(
    guid="c97fc9eb-8ec0-5d06-b4fd-c83ae8a7d1c8",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xatu.Name",
    display_name="Xatu",
    searchable_by=["Xatu", "Stage 1", "Xatu"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Natu.Name",
    family_id=177,
    abilities=[
        Attack(
            title="Fortunate Draw",
            game_text="You and your opponent play Rock-Paper-Scissors. The player who wins draws 3 cards. The player who loses discards the top 3 cards of his or her deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fortunate_draw,
        ),
        Attack(
            title="Miracle Wing",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)