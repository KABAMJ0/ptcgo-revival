from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import Passive, carrier_pokemon

_EVOLVED_STAGES = ("Stage 1", "Stage 2", "VMAX", "BREAK")


def _is_evolved(pokemon) -> bool:
    return any(stage in _EVOLVED_STAGES for stage in subtypes_for(pokemon.archetype_id))


class _Psybarrier(Passive):
    """No attack damage from a non-Evolved attacker; the effects half needs an
    attacker-aware effect shield (filed as a body request)."""

    def prevents_damage(self, calc, carrier):
        attacker = calc.attacker
        return bool(calc.is_attack and calc.is_opposing
                    and calc.target is carrier_pokemon(carrier)
                    and attacker is not None and not _is_evolved(attacker))

card = PokemonCardDef(
    guid="1bf65806-1eef-5a40-9298-a5342ac062b4",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoLVX.Name",
    display_name="Mewtwo LV.X",
    searchable_by=["Mewtwo LV.X", "Level-Up", "MewtwoLVX"],
    subtypes=["Level-Up"],
    collector_number=144,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    family_id=150,
    abilities=[
        Ability(
            title="Psybarrier",
            game_text="Prevent all effects of attacks, including damage, done to Mewtwo by your opponent's Pok\u00e9mon that isn't an Evolved Pok\u00e9mon.",
            passive=_Psybarrier(),
        ),
        Attack(
            title="Giga Burn",
            game_text="Discard all Energy attached to Mewtwo.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)