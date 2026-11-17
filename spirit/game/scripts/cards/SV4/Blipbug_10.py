from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="54621d73-51a8-5f47-b1ff-94559d27ab0b",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blipbug.Name",
    display_name="Blipbug",
    searchable_by=["Blipbug", "Basic", "Blipbug"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=824,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)