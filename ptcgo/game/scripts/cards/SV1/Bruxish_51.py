from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a89538b-0413-525f-ab8b-27dc54e3f048",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bruxish.Name",
    display_name="Bruxish",
    searchable_by=["Bruxish", "Basic", "Bruxish"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=779,
    abilities=[
        Attack(
            title="Vivid Charge",
            game_text="Search your deck for up to 3 Basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(predicate=is_basic_energy_card, count=3, minimum=0),
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)