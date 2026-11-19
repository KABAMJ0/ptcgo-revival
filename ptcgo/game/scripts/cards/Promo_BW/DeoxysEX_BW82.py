from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.passives_common import team_damage_boost_passive
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype
from ptcgo.game.data_utils import def_for
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _plasma_energy_attached(ctx) -> bool:
    return any((getattr(def_for(energy.archetype_id), "display_name", "") or "")
               == "Plasma Energy" for energy in ctx.attached_energies(ctx.attacker))


def _other_team_plasma(attacker) -> bool:
    return attacker is not None and has_pokemon_subtype(attacker, "Team Plasma") \
        and (getattr(def_for(attacker.archetype_id), "display_name", "") or "") \
        != "Deoxys-EX"


def _helix_force_count(ctx) -> int:
    if not _plasma_energy_attached(ctx):
        return 0
    return count_energy("defender")(ctx)


card = PokemonCardDef(
    guid="82294151-0bbb-5a61-b8ea-f834ea49ba88",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysEX.Name",
    display_name="Deoxys-EX",
    searchable_by=["Deoxys-EX", "Basic", "EX", "Team Plasma", "DeoxysEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=82,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Power Connect",
            game_text="Your Team Plasma Pok\u00e9mon's attacks (excluding Deoxys-EX) do 10 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(10, attacker_pred=_other_team_plasma),
        ),
        Attack(
            title="Helix Force",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 30 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(_helix_force_count, 30, base=30),
        ),
    ],
)