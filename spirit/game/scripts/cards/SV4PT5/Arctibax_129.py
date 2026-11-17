from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7839b281-44fc-55c1-bd15-fd1d13c3a098",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name",
    display_name="Arctibax",
    searchable_by=["Arctibax", "Stage 1", "Arctibax"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frigibax.Name",
    family_id=996,
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