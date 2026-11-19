from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _opponents_choice(ctx):
    top = ctx.deck_top(2)
    if len(top) < 2:
        return
    await ctx.reveal_cards(top)
    choice = await ctx.ask_opponent(
        "Choose 1 card for your opponent to put into their hand.",
        ["the first card", "the second card"])
    pick = top[choice if choice in (0, 1) else 0]
    other = top[1] if pick is top[0] else top[0]
    await ctx.put_in_hand([pick], reveal=True)
    await ctx.put_on_bottom_of_deck(other)

card = PokemonCardDef(
    guid="dc6547d0-0e4e-558b-a03e-5f528a14b1f3",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Prime", "Slowking"],
    subtypes=["Stage 1", "Prime"],
    collector_number=85,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Opponent's Choice",
            game_text="Once during your turn (before your attack), you may reveal the top 2 cards of your deck and your opponent chooses 1 of them. Put that card into your hand and the other card on the bottom of your deck. This power can't be used if Slowking is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=_opponents_choice,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
