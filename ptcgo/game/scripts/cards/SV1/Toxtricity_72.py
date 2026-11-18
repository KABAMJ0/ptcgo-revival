import random

from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack


async def _yank_away(ctx):
    """2 random cards out of the opponent's hand, revealed and shuffled back."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    picks = random.sample(hand, min(2, len(hand)))
    await ctx.reveal_cards(picks)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


card = PokemonCardDef(
    guid="0d997fe4-ea63-5a81-939a-d9ca381b5882",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Attack(
            title="Yank Away",
            game_text="Choose 2 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_yank_away,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=recoil_attack(20),
        ),
    ],
)