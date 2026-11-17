from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6d593c7-9719-5a79-b6b4-dffb2252725b",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownU.Name",
    display_name="Unown [U]",
    searchable_by=["Unown [U]", "Basic", "UnownU"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="UNSEEN",
            game_text="As long as Unown U is on your Bench, prevent all effects of attacks, including damage, done by your opponent's Pok\u00e9mon to any Unown on your Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Search your deck for any 1 card and discard it. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)