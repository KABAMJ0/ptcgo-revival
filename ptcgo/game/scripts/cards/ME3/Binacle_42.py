from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0645f96a-e9ce-5cc8-a75c-0cf0a5a3629d",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    display_name="Binacle",
    searchable_by=["Binacle", "Basic", "Binacle"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=688,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)