from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.card_effects.passives_common import free_attack_cost_passive
from ptcgo.game.card_effects.attacks_common import lock_self_attack


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _nine_tools_in_discard(board, pokemon, carrier) -> bool:
    area = board.find_player_area(carrier.owning_player_id, "discard")
    tools = [card for card in (area.children if area else [])
             if card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
    return len(tools) >= 9

card = PokemonCardDef(
    guid="8578c6fe-328d-5de0-bf5a-c67090072aa6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
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
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            effect=lock_self_attack(),
        ),
    ],
)