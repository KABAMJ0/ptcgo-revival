from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.session.effects import is_basic_pokemon

card = PokemonCardDef(
    guid="2aa2c34d-871a-550f-b3c7-b8a3d25f1eae",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    display_name="Poliwag",
    searchable_by=["Poliwag", "Basic", "Poliwag"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=60,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(is_basic_pokemon, count=1),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)