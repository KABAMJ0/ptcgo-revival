from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per


def _plasma_energy_attached(ctx) -> bool:
    return any((getattr(def_for(energy.archetype_id), "display_name", "") or "")
               == "Plasma Energy" for energy in ctx.attached_energies(ctx.attacker))


def _dynamite_press_counters(ctx) -> int:
    if not _plasma_energy_attached(ctx):
        return 0
    return damage_counters_on("defender")(ctx)

card = PokemonCardDef(
    guid="ead03687-f406-5e41-a15f-fddbed22ebef",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranEX.Name",
    display_name="Heatran-EX",
    searchable_by=["Heatran-EX", "Basic", "EX", "Team Plasma", "HeatranEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=109,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Heat Boiler",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Dynamite Press",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=damage_per(_dynamite_press_counters, 10, base=80),
        ),
    ],
)