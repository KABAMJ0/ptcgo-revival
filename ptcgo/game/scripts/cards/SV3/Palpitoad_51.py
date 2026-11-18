from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cdae410-50e2-5f0a-9cb6-a1cbd9a6cf2e",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name",
    display_name="Palpitoad",
    searchable_by=["Palpitoad", "Stage 1", "Palpitoad"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    family_id=535,
    abilities=[
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 2},
            damage=50,
        ),
    ],
)