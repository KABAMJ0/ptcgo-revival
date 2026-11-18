from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a1c8af0-1c38-50ae-ad65-0f10ede99886",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaquaval.Name",
    display_name="Quaquaval",
    searchable_by=["Quaquaval", "Stage 2", "Quaquaval"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SV8",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    family_id=912,
    abilities=[
        Ability(
            title="Up-Tempo",
            game_text="You must put a card from your hand on the bottom of your deck in order to use this Ability. Once during your turn, you may draw cards until you have 5 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)