from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.card_effects.support_common import search_to_bench
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="06bfef1c-674b-51ad-802a-ede559f6f495",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=778,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(count=1),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)