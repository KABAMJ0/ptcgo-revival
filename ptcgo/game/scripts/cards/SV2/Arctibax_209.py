from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5bbeaf04-8254-5a19-82b3-970206f53060",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arctibax.Name",
    display_name="Arctibax",
    searchable_by=["Arctibax", "Stage 1", "Arctibax"],
    subtypes=["Stage 1"],
    collector_number=209,
    set_code="SV2",
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