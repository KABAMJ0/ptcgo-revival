from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e5f03f70-aae8-5833-baf9-db8237abb4c8",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHoundour.Name",
    display_name="Team Rocket's Houndour",
    searchable_by=["Team Rocket's Houndour", "Basic", "TeamRocketsHoundour"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=228,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)