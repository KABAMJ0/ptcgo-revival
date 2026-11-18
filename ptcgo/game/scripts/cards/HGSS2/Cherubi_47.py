from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7bc338f9-8af0-5ae6-8d3b-f41c755b1cfb",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    display_name="Cherubi",
    searchable_by=["Cherubi", "Basic", "Cherubi"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="HGSS2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=420,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)