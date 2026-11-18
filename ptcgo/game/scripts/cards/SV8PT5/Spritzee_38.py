from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7ad46af3-72f3-58e9-bb67-f861c74c4d3f",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    display_name="Spritzee",
    searchable_by=["Spritzee", "Basic", "Spritzee"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SV8PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=682,
    abilities=[
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)