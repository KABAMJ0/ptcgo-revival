from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="19443795-9720-5374-9c00-0e78358b6fe3",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fennekin.Name",
    display_name="Fennekin",
    searchable_by=["Fennekin", "Basic", "Fennekin"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=653,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)