from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import remove_self_from_play


_shuffle_self_into_deck = remove_self_from_play(destination="deck",
                                               with_attachments="same")


async def run_away_draw(ctx):
    if not ctx.deck_top(3):
        return
    await ctx.draw_cards(3)
    await _shuffle_self_into_deck(ctx)


card = PokemonCardDef(
    guid="e284fe70-cebf-5cdc-ad58-f22953274ac3",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dudunsparce.Name",
    display_name="Dudunsparce",
    searchable_by=["Dudunsparce", "Stage 1", "Dudunsparce"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    family_id=206,
    abilities=[
        Ability(
            title="Run Away Draw",
            game_text="Once during your turn, you may draw 3 cards. If you drew any cards in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            effect=run_away_draw,
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)