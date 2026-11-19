from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import smokescreen_attack
from ptcgo.game.card_effects.passives_common import retreat_free_when

def _has_any_energy(pokemon, carrier=None):
    return bool(getattr(pokemon, "children", None))


card = PokemonCardDef(
    guid="ba7a314d-c204-56b4-813b-ceb8dd24e5aa",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=163,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=110,
    abilities=[
        Ability(
            title="Levitate",
            game_text="If this Pok\u00e9mon has any Energy attached to it, this Pok\u00e9mon has no Retreat Cost.",
            passive=retreat_free_when(_has_any_energy),
        ),
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=smokescreen_attack(),
        ),
    ],
)