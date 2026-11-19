from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_pokemon_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="8c1eddcf-1111-5efa-9dc5-8e6d07b72fdc",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic", "Slowpoke"],
    subtypes=["Basic"],
    collector_number=19,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=79,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Tail Lure",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(is_pokemon_card, count=1, minimum=1, reveal=True),
        ),
    ],
)