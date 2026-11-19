from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.card_effects.passives_common import on_ko_from_attack
from ptcgo.game.data_utils import Triggers, def_for

def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


async def shadow_curse_counters(ctx):
    """3 damage counters, placed anywhere on the opponent's side."""
    await ctx.place_damage_counters(3, ctx.opponent_pokemon_in_play())


card = PokemonCardDef(
    guid="30fc2101-e2e0-5b0e-8ec1-83dff32fe87e",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Shadow Curse",
            game_text="If Gengar would be Knocked Out by damage from an opponent's attack, you may put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=on_ko_from_attack(shadow_curse_counters),
        ),
        Attack(
            title="Cursed Reaction",
            game_text="Put 2 damage counters on your opponent's Pok\u00e9mon in any way you like. If Gengar has any React Energy cards attached to it, put 4 damage counters instead.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(lambda c: 4 if _attacker_has_react(c) else 2,
                                target="choose_any_opponent"),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)