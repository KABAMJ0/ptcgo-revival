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


async def _fire_force(ctx):
    """Fire+Lightning basics: Confuse. Fire+Fighting basics: 40 and remove 3
    damage counters from the holder. Otherwise the printed 30."""
    holder = ctx.attacker
    if _has_basic(holder, ctx, PokemonTypes.FIRE, PokemonTypes.LIGHTNING):
        await ctx.deal_damage(30)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    elif _has_basic(holder, ctx, PokemonTypes.FIRE, PokemonTypes.FIGHTING):
        await ctx.deal_damage(40)
        await ctx.heal(30, holder)
    else:
        await ctx.deal_damage(30)


card = PokemonToolCardDef(
    guid="a3d4bb05-9af5-5fd7-b5e4-c5266ebf9123",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere α",
    searchable_by=["Miracle Sphere \u03b1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=129,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Fire Force",
            game_text="If the Pokemon using this attack has Fire and Lightning basic Energy cards attached to it, the Defending Pokemon is now Confused. If it has Fire and Fighting basic Energy cards attached to it, this attack does 30 damage plus 10 more damage and remove 3 damage counters from the holder.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage='30+',
            effect=_fire_force,
        ),
        Ability(
            title="Miracle Sphere \u03b1",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=_evolved_of(PokemonTypes.FIRE, PokemonTypes.LIGHTNING, PokemonTypes.FIGHTING),
)
