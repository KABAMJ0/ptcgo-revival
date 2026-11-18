from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc6a7f11-9bf5-5914-a512-65bb7968b6c8",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownY.Name",
    display_name="Unown [Y]",
    searchable_by=["Unown [Y]", "Basic", "UnownY"],
    subtypes=["Basic"],
    collector_number=81,
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
            title="YAWN",
            game_text="Once during your turn (before your attack), if Unown Y is on your Bench, you may remove 1 damage counter from 1 of your Active Unown and that Unown is now Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            game_text="Search your deck for up to 2 Trainer cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)