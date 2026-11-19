from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.trainers import is_supporter_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="5a38e690-1f9b-56b7-9971-8ba839f32fb7",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name",
    display_name="Piplup",
    searchable_by=["Piplup", "Basic", "Piplup"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=393,
    abilities=[
        Attack(
            title="Call for Support",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_supporter_card, count=1, minimum=1),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)