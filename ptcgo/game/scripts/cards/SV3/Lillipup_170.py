from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d03a3cd1-101d-5f4a-9d1a-c09bbf8977db",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic", "Lillipup"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Rear Kick",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)