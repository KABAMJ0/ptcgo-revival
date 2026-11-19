from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.effects import is_evolution_pokemon
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.attacks_common import conditions_if
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import def_for

def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


card = PokemonCardDef(
    guid="8c2e911a-edcb-5756-93d4-cd7a10745918",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Evolutionary Fan",
            game_text="Once during your turn, when you play Shiftry from your hand to evolve 1 of your Pok\u00e9mon, you may choose 1 of your Evolved Pok\u00e9mon in play (excluding any Shiftry). Return that Pok\u00e9mon and all cards attached to it to your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Reactive Beating",
            game_text="If Shiftry has any React Energy cards attached to it, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=conditions_if(_attacker_has_react, SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Cross-Cut",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, this attack does 40 damage plus 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_evolution_pokemon(ctx.defender), 30),
        ),
    ],
)