from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.support_common import entity_name

_named_exact = lambda *names: (
    lambda card: entity_name(card).lower() in {name.lower() for name in names}
)


card = PokemonCardDef(
    guid="66f3bee1-91b1-5733-8ae3-9c3eb8059710",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningMagikarp.Name",
    display_name="Shining Magikarp",
    searchable_by=["Shining Magikarp", "Basic", "ShiningMagikarp"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Gold Scale",
            game_text="Your opponent may draw 2 cards. Either way, you may draw 2 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Bond",
            game_text="Search your deck for a card named Gyarados, Dark Gyarados, or Shining Gyarados. Show it to your opponent and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_hand(
                _named_exact("gyarados", "dark gyarados", "shining gyarados"),
                count=1,
                reveal=True,
            ),
        ),
    ],
)