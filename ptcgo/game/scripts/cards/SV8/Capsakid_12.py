from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d7d406c8-d8ba-5538-981d-d961dfd62f0d",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    display_name="Capsakid",
    searchable_by=["Capsakid", "Basic", "Capsakid"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=951,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)