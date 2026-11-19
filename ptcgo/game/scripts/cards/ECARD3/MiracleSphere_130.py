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


async def _freezing_force(ctx):
    """Fire+Water basics: 40 and Burned. Water+Psychic basics: shuffle an
    Energy off the Defending Pokemon into the opponent's deck."""
    holder = ctx.attacker
    if _has_basic(holder, ctx, PokemonTypes.FIRE, PokemonTypes.WATER):
        await ctx.deal_damage(40)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    elif _has_basic(holder, ctx, PokemonTypes.WATER, PokemonTypes.PSYCHIC):
        await ctx.deal_damage(30)
        energies = ctx.attached_energies(ctx.defender)
        if energies:
            picks = await ctx.choose_cards(
                energies, 1, minimum=1,
                prompt="Choose an Energy card attached to the Defending Pokemon")
            if picks:
                await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    else:
        await ctx.deal_damage(30)


card = PokemonToolCardDef(
    guid="b3449b56-08c4-5ed5-b680-0d0609437ac7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere β",
    searchable_by=["Miracle Sphere \u03b2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=130,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Freezing Force",
            game_text="If the Pokemon using this attack has Fire and Water basic Energy cards attached to it, this attack does 30 damage plus 10 more damage and the Defending Pokemon is now Burned. If it has Water and Psychic basic Energy cards attached to it, choose an Energy card attached to the Defending Pokemon and your opponent shuffles it into their deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage='30+',
            effect=_freezing_force,
        ),
        Ability(
            title="Miracle Sphere \u03b2",
            game_text="Discard this card at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_tool_at_end_of_turn(),
        ),
    ],
    attach_to=_evolved_of(PokemonTypes.FIRE, PokemonTypes.WATER, PokemonTypes.PSYCHIC),
)
