from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.card_effects.passives_common import heal_activation
from ptcgo.game.data_utils import Triggers, def_for
from ptcgo.game.attributes import AttrID

def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


async def _reactive_healing(ctx):
    """Attaching a React Energy from hand strips every damage counter."""
    receiver = ctx.energy_receiver if ctx.energy_receiver is not None else ctx.source
    if receiver is None or not _is_react(ctx.attached_energy):
        return
    damage = ctx.max_hp(receiver) - receiver.get_attribute(AttrID.HP, 0)
    if damage > 0:
        await ctx.heal(damage, receiver)


card = PokemonCardDef(
    guid="f2bb927d-a029-58aa-9846-b7ebdef44b38",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic", "Tangela"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=114,
    abilities=[
        Ability(
            title="Reactive Healing",
            game_text="Whenever you attach a React Energy card from your hand to Tangela, remove all damage counters from Tangela.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=_reactive_healing,
        ),
        Attack(
            title="Entangling Vines",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, that Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Wrap",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=no_retreat_attack(),
        ),
    ],
)