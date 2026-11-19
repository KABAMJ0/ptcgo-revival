from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_stadium_card
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="89d00e69-d879-575c-a0fa-a25bb2fe797b",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    display_name="Trapinch",
    searchable_by=["Trapinch", "Basic", "Trapinch"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=328,
    abilities=[
        Attack(
            title="Nest Building",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_stadium_card, count=1, reveal=True),
        ),
        Attack(
            title="Sand Spray",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)