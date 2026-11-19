from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="881bd289-b918-56bd-bcf1-edded9689553",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    display_name="Snom",
    searchable_by=["Snom", "Basic", "Snom"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=872,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_bench(),
        ),
    ],
)