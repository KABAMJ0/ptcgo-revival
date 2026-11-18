from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a3dafe1e-4a6d-5b6a-816a-c2ce04ab19b4",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    display_name="Nacli",
    searchable_by=["Nacli", "Basic", "Nacli"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=932,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)