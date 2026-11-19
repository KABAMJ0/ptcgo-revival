from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b23f2d32-0f38-5295-98a6-41c823c10b82",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salazzle.Name",
    display_name="Salazzle",
    searchable_by=["Salazzle", "Stage 1", "Salazzle"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    family_id=757,
    abilities=[
        Attack(
            title="Nasty Plot",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_hand(None, count=2, reveal=False),
        ),
        Attack(
            title="Severe Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 4 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)