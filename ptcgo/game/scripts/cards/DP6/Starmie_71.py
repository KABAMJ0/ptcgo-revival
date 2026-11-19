from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.support_common import remove_self_from_play
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, def_for
from ptcgo.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities


def _has_poke_power_or_body(pokemon) -> bool:
    """The corpus types these DP-era Poké-Powers as POKE_ABILITY, so all three
    of POKE_ABILITY / POKE_POWER / POKE_BODY count as the printed gate."""
    definition = def_for(getattr(pokemon, "archetype_id", "") or "")
    return any(getattr(entry, "ability_type", None) in (AbilityTypes.POKE_ABILITY,
                                                        AbilityTypes.POKE_POWER,
                                                        AbilityTypes.POKE_BODY)
               for entry in getattr(definition, "abilities", None) or [])

card = PokemonCardDef(
    guid="e62b0f90-249a-5a5a-8718-864e6155d7e7",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Attack(
            title="Star Boomerang",
            game_text="You may return Starmie and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=remove_self_from_play(destination="hand", optional=True),
        ),
        Attack(
            title="Core Flash",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any Pok\u00e9-Powers or Pok\u00e9-Bodies. This attack does 50 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=snipe_attack(50, pool=_has_poke_power_or_body, count=1),
        ),
    ],
)