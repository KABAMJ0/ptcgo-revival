from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="503e2812-6aab-5151-bfb9-6e2fd2f93349",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="Talon Hunt",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=search_to_hand(None, count=2, reveal=False),
        ),
    ],
)