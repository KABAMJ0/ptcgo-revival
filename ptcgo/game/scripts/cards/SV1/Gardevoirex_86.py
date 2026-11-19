from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import cure_conditions_effect
from ptcgo.game.session.passives import is_basic_energy


def _basic_psychic_energy(card):
    return is_basic_energy(card) and energy_provides_type(
        card, PokemonTypes.PSYCHIC.value)


def _can_embrace(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.PSYCHIC.value not in types:
        return False
    return pokemon.get_attribute(AttrID.HP, 0) > 20


def _embrace_available(board, player_id, pokemon):
    area = board.find_player_area(player_id, "discard")
    if not any(_basic_psychic_energy(card)
               for card in (area.children if area else [])):
        return False
    return any(_can_embrace(p) for p in board.pokemon_in_play(player_id))


async def _psychic_embrace(ctx):
    energies = [card for card in ctx.discard_pile()
                if _basic_psychic_energy(card)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose a Basic Psychic Energy card to attach")
    if not picks:
        return
    holders = [p for p in ctx.my_pokemon_in_play() if _can_embrace(p)]
    if not holders:
        return
    holder = holders[0] if len(holders) == 1 else await ctx.choose_pokemon(
        holders, "Choose a Psychic Pok\u00e9mon to attach the Energy to")
    if holder is None:
        return
    await ctx.attach_energy(picks[0], holder)
    await ctx.place_damage_counters(2, [holder])


card = PokemonCardDef(
    guid="3b699d00-6d5e-5ef3-95b5-91297e273619",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name",
    display_name="Gardevoir ex",
    searchable_by=["Gardevoir ex", "Stage 2", "ex", "Gardevoirex"],
    subtypes=["Stage 2", "ex"],
    collector_number=86,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    abilities=[
        Ability(
            title="Psychic Embrace",
            game_text="As often as you like during your turn, you may attach a Basic Psychic Energy card from your discard pile to 1 of your Psychic Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, put 2 damage counters on that Pok\u00e9mon. You can't use this Ability on a Pok\u00e9mon that would be Knocked Out.",
            effect=_psychic_embrace,
            activation=Activations.UNLIMITED,
            condition=_embrace_available,
        ),
        Attack(
            title="Miracle Force",
            game_text="This Pok\u00e9mon recovers from all Special Conditions.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=cure_conditions_effect(scope="active"),
        ),
    ],
)