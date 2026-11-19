from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.session.effects import is_pokemon_card


def _type_name(value) -> str:
    """The client name of one Pokemon type value (10 -> 'Psychic')."""
    try:
        return PokemonTypes(int(value)).name.capitalize()
    except ValueError:
        return ""


async def _question(ctx):
    """? : the opponent guesses the type of a face-down Pokemon from hand."""
    hand = [c for c in ctx.hand() if is_pokemon_card(c)]
    if not hand:
        return
    picked = await ctx.choose_cards(hand, 1, prompt="Choose a Pokemon")
    if not picked:
        return
    card = picked[0]
    options = [t.capitalize() for t in _TYPE_NAMES]
    guess = await ctx.ask_opponent("Guess the type of that Pokemon", options)
    actual = {_type_name(v) for v in (card.get_attribute(AttrID.POKEMON_TYPES) or [])}
    await ctx.reveal_cards([card], to_player=ctx.opponent_id)
    if options[guess] not in actual:
        await ctx.draw_cards(1)


async def _hidden_power_cycle(ctx):
    """Hidden Power (Unown ?): discard up to 2 cards, draw one per discard."""
    hand = list(ctx.hand())
    discarded = []
    if hand:
        discarded = await ctx.choose_cards(hand, 2, minimum=0,
                                           prompt="Discard up to 2 cards")
    if discarded:
        await ctx.discard_cards(discarded)
    if discarded:
        await ctx.draw_cards(len(discarded))


_TYPE_NAMES = ["Colorless", "Darkness", "Fairy", "Fighting", "Fire", "Grass",
               "Lightning", "Metal", "Psychic", "Water", "Dragon"]

card = PokemonCardDef(
    guid="21b76a27-7bd2-5a06-8200-a8572810e378",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown [?]",
    searchable_by=["Unown [?]", "Basic", "Unown"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="?",
            game_text="Once during your turn (before your attack), if Unown ? is on your Bench, you may choose a Pok\u00e9mon in your hand and put it face down. Your opponent guesses a type of that Pok\u00e9mon. Reveal that card. If your opponent guessed wrong, draw a card. Then, put that card back into your hand.",
                        activation=Activations.ONCE_PER_TURN,
                        condition=lambda board, player_id, pokemon: not is_in_active_spot(pokemon),
            effect=_question,
        ),
        Attack(
            title="Hidden Power",
            game_text="Discard up to 2 cards from your hand. For each card you discarded, draw a card.",
            cost={},
            effect=_hidden_power_cycle,
        ),
    ],
)