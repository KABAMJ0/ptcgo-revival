from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="06f78b00-363d-5ed1-b9ba-2c60b1e10481",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    display_name="Fomantis",
    searchable_by=["Fomantis", "Basic", "Fomantis"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=753,
    abilities=[
        Attack(
            title="Cut Up",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)