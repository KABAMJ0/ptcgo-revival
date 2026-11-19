from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.content.definitions import Activations

def _psychic_or_metal_energy(card):
    return any(energy_provides_type(card, member.value)
               for member in (PokemonTypes.PSYCHIC, PokemonTypes.METAL))


def _active_only(pokemon):
    return True


geotech_system = attach_from_discard(
    _psychic_or_metal_energy, count=1, target=_active_only, minimum=1,
    prompt="Choose a Psychic or Metal Energy to attach to your Active Pok\u00e9mon")


def _geotech_offered(board, player_id, pokemon):
    area = board.find_player_area(player_id, "discard")
    active = board.active_pokemon(player_id)
    return active is not None and any(
        _psychic_or_metal_energy(card)
        for card in (area.children if area else []))


card = PokemonCardDef(
    guid="7fd15780-e4f3-5966-b11e-3c6118a53140",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MetagrossGX.Name",
    display_name="Metagross-GX",
    searchable_by=["Metagross-GX", "Stage 2", "GX", "MetagrossGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=139,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Geotech System",
            game_text="Once during your turn (before your attack), you may attach a Psychic or Metal Energy card from your discard pile to your Active Pok\u00e9mon.",
            effect=geotech_system,
            activation=Activations.ONCE_PER_TURN,
            condition=_geotech_offered,
        ),
        Attack(
            title="Giga Hammer",
            game_text="This Pok\u00e9mon can't use Giga Hammer during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
        Attack(
            title="Algorithm-GX",
            game_text="Search your deck for up to 5 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(None, count=5, minimum=0, reveal=False),
        ),
    ],
)