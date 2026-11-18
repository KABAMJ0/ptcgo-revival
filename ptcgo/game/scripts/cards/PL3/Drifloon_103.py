from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd64f71c-b49b-5f4f-97d9-3ee16c74e61b",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=425,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="Drifloon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)