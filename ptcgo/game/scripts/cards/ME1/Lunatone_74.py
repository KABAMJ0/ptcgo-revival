from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import discard_from_hand_then
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.card_effects.trainers import basic_energy_of

_BASIC_FIGHTING = basic_energy_of("fighting")


def _lunar_cycle_condition(board, player_id, pokemon) -> bool:
    """Solrock in play and a Basic Fighting Energy in hand to pay with."""
    if not any(mon.archetype_id
               and getattr(def_for(mon.archetype_id), "display_name", "") == "Solrock"
               for mon in board.pokemon_in_play(player_id)):
        return False
    hand = board.find_player_area(player_id, "hand")
    return any(_BASIC_FIGHTING(card) for card in (hand.children if hand else []))


card = PokemonCardDef(
    guid="b07c40c6-f621-54ca-b3aa-52bb7402ec7c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=337,
    abilities=[
        Ability(
            title="Lunar Cycle",
            game_text="Once during your turn, if you have Solrock in play, you may discard a Basic Fighting Energy card from your hand in order to use this Ability. Draw 3 cards. You can't use more than 1 Lunar Cycle Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            effect=discard_from_hand_then(_BASIC_FIGHTING, 1, then=draw_attack(3)),
            condition=_lunar_cycle_condition,
            shared_once_per_turn="Lunar Cycle",
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)