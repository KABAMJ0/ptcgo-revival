from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f0f7256d-6c92-5d3e-a544-35a2f084e20f",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SurfingPikachu.Name",
    display_name="Surfing Pikachu",
    searchable_by=["Surfing Pikachu", "Basic", "SurfingPikachu"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="PL2",
    rarity=Rarities.RareSecret,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Surf",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)