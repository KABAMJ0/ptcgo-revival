from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.data_utils import Activations, def_for
from ptcgo.game.attributes import AttrID

def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


def _reactive_shift_condition(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    return can_move_energy(_is_react)(board, player_id, pokemon)


card = PokemonCardDef(
    guid="ccca713f-efd7-5b39-bf8d-a7344a0ec867",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Reactive Shift",
            game_text="Once during your turn (before your attack), you may move a React Energy card attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Delcatty is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_reactive_shift_condition,
            effect=move_energy_between(predicate=_is_react, count=1, from_pool="any", to_pool="any"),
        ),
        Attack(
            title="Energy Link",
            game_text="Search your discard pile for an Energy card and attach it to Delcatty.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Tail Whap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)