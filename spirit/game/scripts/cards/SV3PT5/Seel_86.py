from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dd942474-d313-59c9-960d-81d0136fa6f1",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    display_name="Seel",
    searchable_by=["Seel", "Basic", "Seel"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=86,
    abilities=[
        Attack(
            title="Chilly",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)