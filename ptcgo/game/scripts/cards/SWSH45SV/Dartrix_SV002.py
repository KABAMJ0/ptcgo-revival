from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d65d99f-6c3c-519f-92ce-684a7c2a8e01",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    display_name="Dartrix",
    searchable_by=["Dartrix", "Stage 1", "Dartrix"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
        ),
    ],
)