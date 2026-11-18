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

card = PokemonCardDef(
    guid="5f353973-462f-5be2-8f68-b906dd41051b",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Prime", "Yanmega"],
    subtypes=["Stage 1", "Prime"],
    collector_number=98,
    set_code="HGSS4",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Ability(
            title="Insight",
            game_text="If you have the same number of cards in your hand as your opponent, the attack cost of each of Yanmega's attacks is 0.",
            passive=free_attack_cost_passive(condition=_hand_sizes_equal),
        ),
        Attack(
            title="Linear Attack",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Sonicboom",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)