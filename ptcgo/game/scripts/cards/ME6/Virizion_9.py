from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="41720a2f-0370-5c40-af56-af0951018ba6",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion", "Basic", "Virizion"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=640,
    abilities=[
        Attack(
            title="Double Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)