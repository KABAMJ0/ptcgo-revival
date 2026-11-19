from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="4a82052b-5b4b-58e2-bb15-a333e11a557f",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic", "Dunsparce"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=1),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)