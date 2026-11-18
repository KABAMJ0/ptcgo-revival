from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c082942d-5662-556e-86a6-b4912034c086",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="ME3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)