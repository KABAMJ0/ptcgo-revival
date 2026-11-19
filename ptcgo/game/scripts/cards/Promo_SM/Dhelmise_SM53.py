from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import team_damage_boost_passive


def _is_metal(pokemon) -> bool:
    return PokemonTypes.METAL.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="7ac89f64-5e0f-5dc9-846b-db66b69015d0",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name",
    display_name="Dhelmise",
    searchable_by=["Dhelmise", "Basic", "Dhelmise"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=781,
    abilities=[
        Ability(
            title="Steelworker",
            game_text="Your Metal Pok\u00e9mon's attacks do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(10, attacker_pred=_is_metal),
        ),
        Attack(
            title="Anchor Shot",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=no_retreat_attack(),
        ),
    ],
)