from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96f5afe5-9309-5bb2-b3e7-4d3d4a58fb9a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    display_name="Shroodle",
    searchable_by=["Shroodle", "Basic", "Shroodle"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=944,
    abilities=[
        Attack(
            title="Spray Fluid",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)