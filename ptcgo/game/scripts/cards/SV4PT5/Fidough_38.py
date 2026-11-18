from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dda16fcf-c0d6-5410-909a-4a156178b2ee",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name",
    display_name="Fidough",
    searchable_by=["Fidough", "Basic", "Fidough"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=926,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)