from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.session.passives import is_basic_energy


def _basic_fighting_energy(card):
    return is_basic_energy(card) and energy_provides_type(
        card, PokemonTypes.FIGHTING.value)


def _basic_fighting_pokemon(pokemon):
    return is_basic_pokemon(pokemon) and PokemonTypes.FIGHTING.value in (
        pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


def _dino_cry_offered(board, player_id, pokemon):
    area = board.find_player_area(player_id, "discard")
    if not any(_basic_fighting_energy(card)
               for card in (area.children if area else [])):
        return False
    return any(_basic_fighting_pokemon(p) for p in board.pokemon_in_play(player_id))


dino_cry = attach_from_discard(
    _basic_fighting_energy, count=2, target=_basic_fighting_pokemon,
    minimum=0, distribute=True,
    prompt="Choose up to 2 Basic Fighting Energy cards to attach")


card = PokemonCardDef(
    guid="a05f01ba-fdd6-5e5e-8eca-9e3280cc3daa",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex", "Koraidonex"],
    subtypes=["Basic", "ex"],
    collector_number=125,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Ability(
            title="Dino Cry",
            game_text="Once during your turn, you may attach up to 2 Basic Fighting Energy cards from your discard pile to your Basic Fighting Pok\u00e9mon in any way you like. If you use this Ability, your turn ends.",
            effect=dino_cry,
            activation=Activations.ONCE_PER_TURN,
            ends_turn=True,
            condition=_dino_cry_offered,
        ),
        Attack(
            title="Wild Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=lock_self_attack(),
        ),
    ],
)