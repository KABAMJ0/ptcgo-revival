from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import evolves_from
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

_MAGIKARP = "com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name"


def _evolves_from_magikarp(card) -> bool:
    return bool(card.archetype_id) and evolves_from(card.archetype_id, _MAGIKARP)

card = PokemonCardDef(
    guid="8ca7dc98-9308-5cb7-a6d4-57e9d2f5b010",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Flip a coin. If heads, search your deck for a card that evolves from Magikarp, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(then=search_to_hand(_evolves_from_magikarp, count=1)),
        ),
        Attack(
            title="Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
