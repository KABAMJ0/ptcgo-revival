from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="005f77f3-71c6-5172-8929-4cf9893c161b",
    key="SMP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AshsPikachu.Name",
    display_name="Ash's Pikachu",
    searchable_by=["Ash's Pikachu", "Basic", "AshsPikachu"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SMP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=25,
    abilities=[
        Attack(
            title="Iron Tail",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderbolt",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)