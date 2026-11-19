from ptcgo.game.data_utils import PokemonToolCardDef, Attack, Ability, Triggers, subtypes_for
from ptcgo.game.attributes import AttrID, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.session.effects import is_pokemon_card
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.trainers import (
    discard_tool_at_end_of_turn, is_basic_energy_card,
)

_EVOLVED = ("Stage 1", "Stage 2", "VMAX", "BREAK")


def _evolved_of(*types):
    values = {t.value for t in types}

    def predicate(card):
        if not is_pokemon_card(card):
            return False
        if not any(stage in _EVOLVED for stage in subtypes_for(card.archetype_id)):
            return False
        return bool(values & set(card.get_attribute(AttrID.POKEMON_TYPES) or []))
    return predicate


def _has_basic(pokemon, ctx, *types):
    """Whether `pokemon` has a basic Energy of every listed type attached."""
    attached = [e for e in ctx.attached_energies(pokemon)
                if is_basic_energy_card(e)]
    return all(any(energy_provides_type(e, t.value) for e in attached)
               for t in types)


async def _thunder_force(ctx):
    """Grass+Lightning basics: Asleep and Poisoned. Water+Lightning basics:
    40 and 1 damage counter on each of the opponent's Benched Pokemon."""
    holder = ctx.attacker
    if _has_basic(holder, ctx, PokemonTypes.GRASS, PokemonTypes.LIGHTNING):
        await ctx.deal_damage(30)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    elif _has_basic(holder, ctx, PokemonTypes.WATER, PokemonTypes.LIGHTNING):
        await ctx.deal_damage(40)
        bench = ctx.opponent_bench()
        if bench:
            await ctx.place_damage_counters(len(bench), bench)
    else:
        await ctx.deal_damage(30)


card = PokemonToolCardDef(
    guid="3ffafd21-663f-59fb-b757-499119bed57a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere γ",
    searchable_by=["Miracle Sphere \u03b3", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=131,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Thunder Force",
            game_text="If the Pokemon using this attack has Grass and Lightning basic Energy cards attached to it, the Defending Pokemon is now Asleep and Poisoned. If it has Water and Lightning basic Energy cards attached to it, this attack does 30 damage plus 10 more damage and put 1 damage counter on each of your opponent's Benched Pokemon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage='30+',
            effect=_thunder_force,
        ),
        Ability(
            title="Miracle Sphere \u03b3",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=_evolved_of(PokemonTypes.GRASS, PokemonTypes.WATER, PokemonTypes.LIGHTNING),
)
