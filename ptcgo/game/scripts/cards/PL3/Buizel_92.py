from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b3c97cb-4a86-58ee-981e-473d5cae40ef",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buizel.Name",
    display_name="Buizel",
    searchable_by=["Buizel", "Basic", "Buizel"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=418,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)