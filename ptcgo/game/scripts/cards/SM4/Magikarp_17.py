from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import evolve_from_deck_attack
from ptcgo.game.card_effects.passives_common import is_in_active_spot, prevent_damage_when


def _protects_benched_self(calc, carrier) -> bool:
    return calc.target is carrier and not is_in_active_spot(carrier)


card = PokemonCardDef(
    guid="6bbdafd3-bfea-5ce5-af64-bf7ee67e4e58",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            passive=prevent_damage_when(_protects_benched_self),
        ),
        Attack(
            title="Waterfall Evolution",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=evolve_from_deck_attack(),
        ),
    ],
)