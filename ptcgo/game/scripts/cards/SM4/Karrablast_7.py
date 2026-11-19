from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import pokemon_named


def _shell_on_available(board, player_id, pokemon=None) -> bool:
    """Offerable only with a Shelmet in hand and this Pokemon's evolution in
    the deck: the whole body is a discard cost plus that search."""
    is_shelmet = pokemon_named("Shelmet")
    hand = board.find_player_area(player_id, "hand")
    if not any(is_shelmet(card) for card in (hand.children if hand else [])):
        return False
    deck = board.find_player_area(player_id, "deck")
    logic_name = pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) if pokemon else None
    return any(card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic_name
               for card in (deck.children if deck else []))


async def shell_on(ctx):
    """Discard a Shelmet from hand; search the deck for a card that evolves
    from this Pokemon and put it onto it, then shuffle."""
    is_shelmet = pokemon_named("Shelmet")
    shelmets = [card for card in ctx.hand() if is_shelmet(card)]
    if not shelmets:
        return
    picks = await ctx.choose_cards(
        shelmets, 1, prompt="Choose a Shelmet to discard")
    if not picks:
        return
    await ctx.discard_cards(picks)
    me = ctx.source
    logic_name = me.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    found = await ctx.search_deck(
        lambda card: card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == logic_name,
        count=1, minimum=0, prompt="Choose a card that evolves from this Pokémon")
    if found:
        await ctx.evolve_pokemon(me, found[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="f73fad69-6778-54dd-9ab2-42aaa900f5c7",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    display_name="Karrablast",
    searchable_by=["Karrablast", "Basic", "Karrablast"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=588,
    abilities=[
        Ability(
            title="Shell On",
            game_text="Once during your turn (before your attack), you may discard a Shelmet from your hand. If you do, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_shell_on_available,
            effect=shell_on,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)