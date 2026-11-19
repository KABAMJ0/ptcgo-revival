from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import gust_then
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import Triggers, def_for
from ptcgo.game.attributes import AttrID

async def poison_new_defender(ctx, pokemon):
    await ctx.apply_special_condition(pokemon, SpecialConditions.POISONED)


def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


async def _reactive_aroma(ctx):
    """Checkup: remove 1 damage counter from each of your Pokemon that has a
    React Energy attached."""
    if ctx.source is None:
        return
    for pokemon in ctx.my_pokemon_in_play():
        if _react_count(pokemon) and pokemon.get_attribute(AttrID.HP, 0) < ctx.max_hp(pokemon):
            await ctx.heal(10, pokemon)


card = PokemonCardDef(
    guid="1d1dcf44-e942-5c93-ba4d-a88a362bb4b1",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic", "Roselia"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Ability(
            title="Reactive Aroma",
            game_text="As long as Roselia has any React Energy cards attached to it, remove 1 damage counter from each of your Pok\u00e9mon (excluding Pok\u00e9mon-ex) that has any React Energy cards attached to it between turns. You can't use more than 1 Reactive Aroma Pok\u00e9-Body each turn.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=_reactive_aroma,
        ),
        Attack(
            title="Flick Poison",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_then(poison_new_defender, opponent_chooses=True),
        ),
    ],
)