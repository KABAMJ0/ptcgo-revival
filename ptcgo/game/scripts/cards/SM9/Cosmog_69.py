from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import is_in_active_spot, prevent_damage_when


def _protects_benched_self(calc, carrier) -> bool:
    return calc.target is carrier and not is_in_active_spot(carrier)


card = PokemonCardDef(
    guid="bdd4b3c7-7dc5-5631-9afe-63c89914d814",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name",
    display_name="Cosmog",
    searchable_by=["Cosmog", "Basic", "Cosmog"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=789,
    abilities=[
        Ability(
            title="Cosmic Guard",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage done to this Pok\u00e9mon by attacks (both yours and your opponent's).",
            passive=prevent_damage_when(_protects_benched_self),
        ),
        Attack(
            title="Mumble",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)