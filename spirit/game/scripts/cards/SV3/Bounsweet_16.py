from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccb73a9d-239b-520c-8300-8299ca9b14a3",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name",
    display_name="Bounsweet",
    searchable_by=["Bounsweet", "Basic", "Bounsweet"],
    subtypes=["Basic"],
    collector_number=16,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=761,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)