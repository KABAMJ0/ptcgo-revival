from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, TrainerType
from ptcgo.game.card_effects.attacks_common import discard_for_bonus, no_retreat_attack

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_tool(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES

card = PokemonCardDef(
    guid="1523d809-b163-5192-b7c3-e3a707ba9c1f",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Cofagrigus"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Attack(
            title="Chuck",
            game_text="Discard as many Pok\u00e9mon Tool cards as you like from your hand. This attack does 40 damage times the number of cards you discarded.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="x",
            effect=discard_for_bonus(source="hand", predicate=_is_tool, max_count=10,
                                     per=40, base=0),
        ),
        Attack(
            title="Lock Up",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=no_retreat_attack(),
        ),
    ],
)