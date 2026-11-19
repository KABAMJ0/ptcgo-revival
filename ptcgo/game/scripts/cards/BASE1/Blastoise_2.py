from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_per_extra_energy
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import requires_hand, requires_in_play
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.data_utils import Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


def _water_energy_card(card):
    return is_basic_energy_card(card) \
        and energy_provides_type(card, PokemonTypes.WATER.value)


def _water_pokemon(pokemon):
    return PokemonTypes.WATER.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _can_rain_dance(board, player_id, pokemon=None):
    return (requires_hand(_water_energy_card, 1, exclude_self=False)(board, player_id, pokemon)
            and requires_in_play(_water_pokemon, "mine")(board, player_id, pokemon))


async def rain_dance(ctx):
    energies = [card for card in ctx.hand() if _water_energy_card(card)]
    targets = [p for p in ctx.my_pokemon_in_play() if _water_pokemon(p)]
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(
        energies, 1, minimum=1, prompt="Choose a Water Energy card to attach.")
    if not picks:
        return
    holder = await ctx.choose_pokemon(targets, "Choose a Pok\u00e9mon to attach it to")
    if holder is not None:
        await ctx.attach_energy(picks[0], holder)

card = PokemonCardDef(
    guid="4e52b95c-0803-5fb1-88bb-d1d9b5cfad66",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Rain Dance",
            game_text="As often as you like during your turn (before your attack), you may attach 1 Water Energy card to 1 of your Water Pok\u00e9mon. (This doesn't use up your 1 Energy card attachment for the turn.) This power can't be used if Blastoise is Asleep, Confused, or Paralyzed.",
            activation=Activations.UNLIMITED,
            condition=_can_rain_dance,
            effect=rain_dance,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 40 damage plus 10 more damage for each Water Energy attached to Blastoise but not used to pay for this attack's Energy cost. Extra Water Energy after the 2nd doesn't count.",
            cost={PokemonTypes.WATER: 3},
            damage=40,
            damage_operator="+",
            effect=damage_per_extra_energy(10, energy_type=PokemonTypes.WATER, cap=20),
        ),
    ],
)