from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import free_attack_cost_passive


def _hand_count(board, player_id) -> int:
    area = board.find_player_area(player_id, "hand")
    return len(area.children) if area else 0


def _hand_sizes_equal(board, pokemon, carrier) -> bool:
    mine = carrier.owning_player_id
    other = next((p for p in board.player_ids if p != mine), None)
    return other is not None and _hand_count(board, mine) == _hand_count(board, other)


def _hand_is_four(board, pokemon, carrier) -> bool:
    return _hand_count(board, carrier.owning_player_id) == 4
from ptcgo.game.card_effects.attacks_common import bonus_if, active_is, has_tool


card = PokemonCardDef(
    guid="79359273-8c2c-5dc6-8bae-d9be2e690d1f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Yanmega"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=469,
    abilities=[
        Ability(
            title="Sonic Vision",
            game_text="If you have exactly 4 cards in your hand, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            passive=free_attack_cost_passive(condition=_hand_is_four),
        ),
        Attack(
            title="Assault Boom",
            game_text="If your opponent's Active Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=bonus_if(active_is(has_tool), 70),
        ),
    ],
)