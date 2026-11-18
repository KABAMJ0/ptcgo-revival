from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="728f4ca3-ecff-5968-b823-0a55f31e3d18",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=278,
    abilities=[
        Attack(
            title="Spit Up",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)