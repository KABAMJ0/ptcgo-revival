from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a4ba63ed-1d41-5bd8-be94-ed52bbc8bfc3",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiant.Name",
    display_name="Iron Valiant",
    searchable_by=["Iron Valiant", "Basic", "Future", "IronValiant"],
    subtypes=["Basic", "Future"],
    collector_number=80,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Attack(
            title="Calculation",
            game_text="Look at the top 4 cards of your deck and put them back in any order.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Majestic Sword",
            game_text="If you played a Future Supporter card from your hand during this turn, this attack does 100 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)