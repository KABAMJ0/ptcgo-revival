from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11cd48e6-e60a-5fd4-bc91-b5d9deb02678",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Floragato.Name",
    display_name="Floragato",
    searchable_by=["Floragato", "Stage 1", "Floragato"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sprigatito.Name",
    family_id=906,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)