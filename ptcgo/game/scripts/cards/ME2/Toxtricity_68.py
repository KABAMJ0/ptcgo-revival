from ptcgo.game.data_utils import (
    Activations, PokemonCardDef, Attack, Ability, unimplemented,
)
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import is_basic_energy_card


def _is_basic_darkness_energy(card) -> bool:
    return (is_basic_energy_card(card)
            and energy_provides_type(card, PokemonTypes.DARKNESS.value))


def _is_benched_darkness(pokemon) -> bool:
    return (not is_in_active_spot(pokemon)
            and PokemonTypes.DARKNESS.value
            in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or []))


def _sinister_surge_condition(board, player_id, pokemon) -> bool:
    """A Basic Darkness Energy in the deck and a Benched Darkness Pokemon."""
    deck = board.find_player_area(player_id, "deck")
    if not any(_is_basic_darkness_energy(card)
               for card in (deck.children if deck else [])):
        return False
    return any(_is_benched_darkness(p) for p in board.pokemon_in_play(player_id))


async def sinister_surge(ctx):
    """Search a Basic Darkness Energy out of the deck onto a Benched Darkness
    Pokemon, shuffle, then put 2 damage counters on that Pokemon."""
    found = await ctx.search_deck(
        _is_basic_darkness_energy, count=1, minimum=0,
        prompt="Choose a Basic Darkness Energy card to attach")
    holder = None
    targets = [p for p in ctx.my_bench() if _is_benched_darkness(p)]
    if found and targets:
        holder = await ctx.choose_pokemon(
            targets, "Choose a Benched Darkness Pokémon")
        if holder is not None:
            await ctx.attach_energy(found[0], holder)
    await ctx.shuffle_deck()
    if holder is not None:
        await ctx.deal_damage(20, target=holder, as_counters=True,
                              apply_modifiers=False)


card = PokemonCardDef(
    guid="2a577aee-d427-55bf-bb61-0a841a765f76",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Ability(
            title="Sinister Surge",
            game_text="Once during your turn, you may use this Ability. Search your deck for a Basic Darkness Energy card and attach it to 1 of your Benched Darkness Pok\u00e9mon. Then, shuffle your deck. If you attached Energy to a Pok\u00e9mon in this way, place 2 damage counters on that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_sinister_surge_condition,
            effect=sinister_surge,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)