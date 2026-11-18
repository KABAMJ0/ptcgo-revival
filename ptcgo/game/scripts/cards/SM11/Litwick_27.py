from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import pokemon_of

card = PokemonCardDef(
    guid="9ee40ca3-06ce-5ead-9c07-5e58e25e2cef",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    display_name="Litwick",
    searchable_by=["Litwick", "Basic", "Litwick"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=607,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Fire Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=search_to_hand(pokemon_of("fire"), count=1),
        ),
    ],
)