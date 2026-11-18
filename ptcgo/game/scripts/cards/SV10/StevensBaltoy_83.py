from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.trainers import all_of, named

card = PokemonCardDef(
    guid="60cc3ee3-2751-57b0-889f-da7fd60ebaea",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBaltoy.Name",
    display_name="Steven's Baltoy",
    searchable_by=["Steven's Baltoy", "Basic", "StevensBaltoy"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=343,
    abilities=[
        Attack(
            title="Summoning Sign",
            game_text="Search your deck for up to 2 Basic Steven's Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(all_of(is_basic_pokemon, named("steven's")), count=2),
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)