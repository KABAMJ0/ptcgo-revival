from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn


def _attacker_has_ability(attacker):
    """Prints an Ability -- not merely one of its attacks."""
    if attacker is None:
        return False
    printed = getattr(def_for(attacker.archetype_id), "abilities", None) or []
    return any(isinstance(a, Ability) and not isinstance(a, Attack)
               for a in printed)


card = PokemonCardDef(
    guid="f9e4c219-4ebf-56e1-b726-c09ef55e51ce",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic", "Deoxys"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=386,
    abilities=[
        Attack(
            title="Psy Protection",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Pok\u00e9mon that have an Ability.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=protect_next_turn(prevent=True, attacker_pred=_attacker_has_ability),
        ),
    ],
)