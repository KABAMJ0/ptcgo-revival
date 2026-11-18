from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="850843f6-44c1-5f12-b9f0-be16160510b9",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name",
    display_name="Quaxwell",
    searchable_by=["Quaxwell", "Stage 1", "Quaxwell"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    family_id=912,
    abilities=[
        Attack(
            title="Aqua Edge",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
    ],
)