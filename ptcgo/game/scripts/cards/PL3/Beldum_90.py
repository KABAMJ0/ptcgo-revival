from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import is_stadium_card

card = PokemonCardDef(
    guid="f47def68-cdb4-578a-9b1d-c7f39ed54c29",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=374,
    abilities=[
        Attack(
            title="Pit Search",
            game_text="Search your deck for a Stadium card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_stadium_card, count=1, reveal=True),
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)