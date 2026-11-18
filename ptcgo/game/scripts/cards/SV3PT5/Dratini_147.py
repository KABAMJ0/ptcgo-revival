from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7495e482-966b-53dc-aaad-aa1fe479c001",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=147,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Draconic Whip",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
    ],
)