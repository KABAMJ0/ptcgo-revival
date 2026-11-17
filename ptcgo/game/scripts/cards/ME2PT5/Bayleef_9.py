from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d1cb3a9e-cd46-5ea8-b344-080aa220ab31",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    display_name="Bayleef",
    searchable_by=["Bayleef", "Stage 1", "Bayleef"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    family_id=152,
    abilities=[
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
        ),
    ],
)