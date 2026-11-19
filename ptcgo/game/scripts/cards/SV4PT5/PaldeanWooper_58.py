from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import is_stadium_card
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="871fcebf-372c-5bca-bc6b-97d881506dac",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    display_name="Paldean Wooper",
    searchable_by=["Paldean Wooper", "Basic", "PaldeanWooper"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=194,
    abilities=[
        Attack(
            title="Find a Home",
            game_text="Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_stadium_card, count=1, minimum=1, reveal=True),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)