from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e2dc22be-93d6-5f6a-befc-f3ebfd906a50",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=["Gible", "Basic", "Gible"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)