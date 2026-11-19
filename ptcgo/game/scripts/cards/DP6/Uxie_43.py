from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_until_effect
from ptcgo.game.session.effects import full_stack


async def _psychic_restore(ctx):
    """Psychic Restore: may tuck Uxie and its whole stack under the deck."""
    await ctx.deal_damage()
    if not await ctx.ask_yes_no(
            "Put Uxie and all cards attached to it on the bottom of your deck?"):
        return
    pokemon = ctx.attacker
    if pokemon is None:
        return
    was_active = pokemon is ctx.my_active()
    stack = full_stack(pokemon)
    deck = ctx.board.find_player_area(ctx.player_id, "deck")
    for card in stack:
        ctx.board.move_card(card.entity_id, deck.entity_id)
    for card in stack:
        await ctx.shuffle_deck_below(card)
    if was_active:
        await ctx.session._promote_new_active(ctx.player_id)

card = PokemonCardDef(
    guid="60517751-4494-5c78-9ecb-ecd98ce303ce",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic", "Uxie"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=480,
    abilities=[
        Ability(
            title="Set Up",
            game_text="Once during your turn, when you put Uxie from your hand onto your Bench, you may draw cards until you have 7 cards in your hand.",
            trigger=Triggers.ON_PLAY,
            effect=draw_until_effect(7),
        ),
        Attack(
            title="Psychic Restore",
            game_text="You may put Uxie and all cards attached to it on the bottom of your deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_psychic_restore,
        ),
    ],
)