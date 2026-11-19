from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on
from ptcgo.game.data_utils import def_for

def _is_react(card) -> bool:
    definition = def_for(getattr(card, "archetype_id", "") or "")
    return (getattr(definition, "display_name", "") or "").strip().lower() == "react energy"


def _react_count(pokemon) -> int:
    return sum(1 for energy in (getattr(pokemon, "children", None) or [])
               if _is_react(energy))


def _attacker_has_react(ctx) -> bool:
    return ctx.attacker is not None and _react_count(ctx.attacker) > 0


async def _heavy_blow(ctx):
    """70 minus 10 per damage counter on Aggron; a flat 70 with React Energy."""
    if _attacker_has_react(ctx):
        await ctx.deal_damage(70)
        return
    await ctx.deal_damage(max(0, 70 - 10 * damage_counters_on("self")(ctx)))


card = PokemonCardDef(
    guid="dc01c2d9-7198-53b2-b79e-c4d630973bc9",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=2,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Heavy Blow",
            game_text="Does 70 damage minus 10 damage for each damage counter on Aggron. If Aggron has any React Energy cards attached to it, this attack does 70 damage instead.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="-",
            effect=_heavy_blow,
        ),
        Attack(
            title="Bound Crush",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 60 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) During your next turn, Aggron can't use Bound Crush.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(60, pool="any"),
        ),
    ],
)