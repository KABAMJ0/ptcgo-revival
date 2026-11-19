from ptcgo.game.card_effects.trainers import is_item_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="245a379a-c25d-5864-a7f0-20e42db82973",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMareep.Name",
    display_name="Team Rocket's Mareep",
    searchable_by=["Team Rocket's Mareep", "Basic", "TeamRocketsMareep"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=179,
    abilities=[
        Attack(
            title="Procurement",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_item_card, count=1, minimum=1),
        ),
        Attack(
            title="Tiny Bolt",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)