from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.card_effects.passives_common import free_attack_cost_passive


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _nine_tools_in_discard(board, pokemon, carrier) -> bool:
    area = board.find_player_area(carrier.owning_player_id, "discard")
    tools = [card for card in (area.children if area else [])
             if card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
    return len(tools) >= 9
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="bed91645-0fba-5e32-a887-8f2faff9ef05",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic", "MowRotom"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            passive=free_attack_cost_passive(condition=_nine_tools_in_discard),
        ),
        Attack(
            title="Special Mow",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
    ],
)