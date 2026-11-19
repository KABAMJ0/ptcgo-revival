from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.data_utils import def_for
from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
from ptcgo.game.card_effects.trainers import combined, holder_ability_shield


def _hide_n_sneak_in_discard(ctx) -> int:
    """Pokemon in your discard pile that print the Hide 'n' Sneak Ability."""
    return sum(
        1 for card in ctx.discard_pile()
        if any(getattr(ability, "title", "") == "Hide 'n' Sneak"
               for ability in getattr(def_for(card.archetype_id),
                                      "abilities", []) or [])
    )


async def matcha_spin(ctx):
    """With 6+ Hide 'n' Sneak Pokemon in the discard, 4 counters on each of
    the opponent's Pokemon."""
    if _hide_n_sneak_in_discard(ctx) < 6:
        return
    for pokemon in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(40, target=pokemon, as_counters=True,
                              apply_modifiers=False)


card = PokemonCardDef(
    guid="b14ebb0e-39e9-5b5f-9819-b4130448ac65",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistcha.Name",
    display_name="Sinistcha",
    searchable_by=["Sinistcha", "Stage 1", "Sinistcha"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ME5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    family_id=1012,
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's attacks and Abilities done to this Pok\u00e9mon. (Damage is not an effect.)",
            passive=combined(attack_effect_shield_passive(), holder_ability_shield()),
        ),
        Attack(
            title="Matcha Spin",
            game_text="If you have 6 or more Pok\u00e9mon that have the Hide 'n' Sneak Ability in your discard pile, place 4 damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=matcha_spin,
        ),
    ],
)