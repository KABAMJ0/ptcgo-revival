from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def evidence_gathering(ctx):
    """Switch a card from your hand with the top card of your deck."""
    hand = ctx.hand()
    if not hand or not ctx.deck():
        return
    picked = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card from your hand to put on top of your deck",
    )
    if not picked:
        return
    top = ctx.deck_top(1)
    if not top:
        return
    await ctx.put_on_top_of_deck(picked[0])
    await ctx.put_in_hand(top, reveal=False)


card = PokemonCardDef(
    guid="0da3f91a-4465-5947-8e95-929e3e9a3d11",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gumshoos.Name",
    display_name="Gumshoos",
    searchable_by=["Gumshoos", "Stage 1", "Gumshoos"],
    subtypes=["Stage 1"],
    collector_number=153,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    family_id=734,
    abilities=[
        Ability(
            title="Evidence Gathering",
            game_text="Once during your turn, you may use this Ability. Switch a card from your hand with the top card of your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=evidence_gathering,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)