from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import named

card = PokemonCardDef(
    guid="a3b37f0e-c177-5a14-b91f-866eef524a92",
    key="MCD22",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="MCD22",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Wintry Call",
            game_text="Search your deck for up to 2 Melony cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(named("melony"), count=2, reveal=True),
        ),
        Attack(
            title="Icy Wind",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)