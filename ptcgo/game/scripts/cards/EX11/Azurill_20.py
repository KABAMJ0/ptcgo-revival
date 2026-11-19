from ptcgo.game.card_effects.support_common import baby_evolution
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.session.effects import is_basic_pokemon, is_evolution_pokemon, is_special_energy
from ptcgo.game.session.passives import energy_provided_options

_baby_effect, _baby_in_hand = baby_evolution("Marill")


async def _type_match(ctx):
    basics = [card for card in ctx.hand()
              if is_energy_card(card) and not is_special_energy(card)]
    if not basics:
        return
    picked = await ctx.choose_cards(
        basics, 1, minimum=1, prompt="Choose a basic Energy card to show")
    if not picked:
        return
    energy_types = set()
    for option in energy_provided_options(ctx.board, picked[0]):
        energy_types.update(option)
    if not energy_types:
        return

    def matches(card):
        if not (is_basic_pokemon(card, ctx.board) or is_evolution_pokemon(card)):
            return False
        return bool(energy_types & set(card.get_attribute(AttrID.POKEMON_TYPES) or []))

    found = await ctx.search_deck(matches, count=1, minimum=0,
                                  prompt="Choose a Pok\u00e9mon of that Energy type")
    if found:
        await ctx.put_in_hand(found, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="293ecac5-6ab1-5fe9-b515-10b7687cd38a",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill", "Basic", "Azurill"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Marill from your hand onto Azurill (this counts as evolving Azurill) and remove all damage counters from Azurill.",
            activation=Activations.ONCE_PER_TURN,
            condition=_baby_in_hand,
            effect=_baby_effect,
        ),
        Attack(
            title="Type Match",
            game_text="Choose a basic Energy card in your hand and show it to your opponent. Then, search your deck for a Basic Pok\u00e9mon or Evolution card of that Energy type, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_type_match,
        ),
    ],
)