from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="2c5345e4-5fe8-5055-ac12-3d218035e285",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    display_name="Minccino",
    searchable_by=["Minccino", "Basic", "Minccino"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=572,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=1),
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)