from ptcgo.game.card_effects.trainers import is_item_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="845e9dd8-0605-5d89-9504-00ca63176bd1",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    display_name="Patrat",
    searchable_by=["Patrat", "Basic", "Patrat"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=504,
    abilities=[
        Attack(
            title="Procurement",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(predicate=is_item_card, count=1, minimum=1),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)