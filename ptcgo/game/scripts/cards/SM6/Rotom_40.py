from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities, TrainerType
from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
from ptcgo.game.card_effects.attacks_common import lock_self_attack


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _nine_tools_in_discard(board, pokemon, carrier) -> bool:
    area = board.find_player_area(carrier.owning_player_id, "discard")
    tools = [card for card in (area.children if area else [])
             if card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
    return len(tools) >= 9

card = PokemonCardDef(
    guid="377cceb8-ac2b-507e-bbba-f25f4131ba94",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            passive=free_attack_cost_passive(condition=_nine_tools_in_discard),
        ),
        Attack(
            title="Plasma Slice",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=120,
            effect=lock_self_attack(),
        ),
    ],
)