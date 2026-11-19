import random

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _astonish(ctx):
    """Printed damage, then a random card from the opponent's hand is
    revealed and shuffled into their deck."""
    await ctx.deal_damage()
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.shuffle_into_deck([card], ctx.opponent_id)


card = PokemonCardDef(
    guid="7082be1f-ce7f-5489-bc0d-29584ba80b9b",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic", "Pumpkaboo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=710,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_astonish,
        ),
    ],
)