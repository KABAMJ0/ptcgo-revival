from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da46cc5d-d2bf-50d3-8f04-abd9e3bca82b",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownC.Name",
    display_name="Unown [C]",
    searchable_by=["Unown [C]", "Basic", "UnownC"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="CALL",
            game_text="Once during your turn (before your attack), if Unown C is on your Bench, you may flip coin. If heads, search your deck for any 1 Unown and put it onto your Bench. Shuffle your deck afterward.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)