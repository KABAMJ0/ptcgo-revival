from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="41d7efa0-40ad-5d70-b2bd-ffccad65cd8b",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=877,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 Basic Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=2),
        ),
        Attack(
            title="Slap",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
    ],
)