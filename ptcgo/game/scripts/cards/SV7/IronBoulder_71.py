from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18bce158-fce3-52f4-917d-be782d98b6a6",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulder.Name",
    display_name="Iron Boulder",
    searchable_by=["Iron Boulder", "Basic", "Future", "IronBoulder"],
    subtypes=["Basic", "Future"],
    collector_number=71,
    set_code="SV7",
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