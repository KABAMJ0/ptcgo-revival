from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f0450720-dee0-5b09-b13b-237e7f712740",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name",
    display_name="Arctibax",
    searchable_by=["Arctibax", "Stage 1", "Arctibax"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name",
    family_id=997,
    abilities=[
        Attack(
            title="Sharp Fin",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Frost Smash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)