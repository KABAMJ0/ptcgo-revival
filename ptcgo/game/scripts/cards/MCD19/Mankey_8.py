from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb308d5a-ea77-5b1c-adfd-f266663cd47a",
    key="MCD19",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic", "Mankey"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="MCD19",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Three-Step Strike",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)