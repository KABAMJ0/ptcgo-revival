from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.trainers import is_supporter_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="4f2775c2-267d-59c2-a38e-4e0ecca0901e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=166,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_supporter_card, count=1, minimum=1),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)