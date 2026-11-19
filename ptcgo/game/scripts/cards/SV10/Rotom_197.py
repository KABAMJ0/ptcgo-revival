from ptcgo.game.card_effects.attacks_common import damage_per, count_in_play, has_tool
import random

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
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
    guid="5d7d80cd-7f47-5d76-b53f-c7d76b1c97b4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=197,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=_astonish,
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pok\u00e9mon Tool attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", has_tool), 30),
        ),
    ],
)