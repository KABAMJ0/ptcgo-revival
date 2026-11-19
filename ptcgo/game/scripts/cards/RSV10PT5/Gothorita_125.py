from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def fortunate_eye(ctx):
    """Look at the top 5 cards of your opponent's deck and put them back in
    any order."""
    top = ctx.deck_top(5, ctx.opponent_id)
    if len(top) <= 1:
        return
    picked_ids = await ctx.session.prompt_card_chooser(
        ctx.player_id, ctx.source.entity_id, top, len(top), minimum=len(top),
        prompt="Put the cards back in any order.", ordered=True,
    )
    by_id = {c.entity_id: c for c in top}
    order = [by_id[i] for i in picked_ids if i in by_id]
    for card in top:
        if card not in order:
            order.append(card)
    deck = ctx.board.find_player_area(ctx.opponent_id, "deck")
    for card in order:
        deck.children.remove(card)
    for card in reversed(order):
        deck.children.append(card)


card = PokemonCardDef(
    guid="275af2d5-7376-59fd-903b-0f1e7e58d92d",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    display_name="Gothorita",
    searchable_by=["Gothorita", "Stage 1", "Gothorita"],
    subtypes=["Stage 1"],
    collector_number=125,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Fortunate Eye",
            game_text="Look at the top 5 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=fortunate_eye,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)