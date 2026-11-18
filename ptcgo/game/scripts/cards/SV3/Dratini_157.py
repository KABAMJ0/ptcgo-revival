from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="177f13c8-8b7f-5ff3-bec5-350056f131c9",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=147,
    abilities=[
        Attack(
            title="Tail Snap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)