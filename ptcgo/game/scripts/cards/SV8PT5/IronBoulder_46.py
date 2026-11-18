from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4dcf683f-4734-5d73-9bf2-d8792355c336",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulder.Name",
    display_name="Iron Boulder",
    searchable_by=["Iron Boulder", "Basic", "Future", "IronBoulder"],
    subtypes=["Basic", "Future"],
    collector_number=46,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Adjusted Horn",
            game_text="If you don't have the same number of cards in your hand as your opponent, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)