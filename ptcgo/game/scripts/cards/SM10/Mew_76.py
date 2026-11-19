from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.card_effects.passives_common import is_in_active_spot, prevent_damage_when


def _protects_own_bench(calc, carrier) -> bool:
    return (calc.target.owning_player_id == carrier.owning_player_id
            and not is_in_active_spot(calc.target))

card = PokemonCardDef(
    guid="46e5bb52-b8f8-5f91-8e4e-be8cdfcb4074",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM10",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Bench Barrier",
            game_text="Prevent all damage done to your Benched Pok\u00e9mon by your opponent's attacks.",
            passive=prevent_damage_when(_protects_own_bench),
        ),
        Attack(
            title="Psypower",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(3, "choose_any_opponent"),
        ),
    ],
)