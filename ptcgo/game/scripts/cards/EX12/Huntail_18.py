from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_EX
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.attributes import AttrID
from ptcgo.game.card_effects.support_common import search_attach_energy
from ptcgo.game.data_utils import Activations, def_for

def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


def _reactive_generator_condition(board, player_id, pokemon):
    """Only while Huntail has no React Energy of its own and the deck can
    supply one."""
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    if _react_count(pokemon):
        return False
    area = board.find_player_area(player_id, "deck")
    return any(_is_react(card) for card in (area.children if area else []))


card = PokemonCardDef(
    guid="3ef268be-f2ae-5d0d-a1a2-95776d616c52",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1", "Huntail"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Ability(
            title="Reactive Generator",
            game_text="Once during your turn (before your attack), if Huntail has no React Energy cards attached to it, you may search your deck for a React Energy card and attach it to Huntail. Shuffle your deck afterward. This power can't be used if Huntail is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_reactive_generator_condition,
            effect=search_attach_energy(_is_react, count=1, to_self=True),
        ),
        Attack(
            title="Bite Off",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_EX(ctx.defender), 30, base=40),
        ),
    ],
)