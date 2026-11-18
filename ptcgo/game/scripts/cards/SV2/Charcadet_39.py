from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a4ebd1e-8a96-52e6-a6bc-060c0714119f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    display_name="Charcadet",
    searchable_by=["Charcadet", "Basic", "Charcadet"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=935,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Magnum Punch",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)