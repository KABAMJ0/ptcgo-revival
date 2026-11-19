from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from ptcgo.game.card_effects.passives_common import free_attack_cost_passive


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _nine_tools_in_discard(board, pokemon, carrier) -> bool:
    area = board.find_player_area(carrier.owning_player_id, "discard")
    tools = [card for card in (area.children if area else [])
             if card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
    return len(tools) >= 9

card = PokemonCardDef(
    guid="9cb6e492-a03f-5430-a00e-12e4b5adf5c9",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotom.Name",
    display_name="Heat Rotom",
    searchable_by=["Heat Rotom", "Basic", "HeatRotom"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            passive=free_attack_cost_passive(condition=_nine_tools_in_discard),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)