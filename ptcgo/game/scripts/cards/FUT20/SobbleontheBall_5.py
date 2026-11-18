from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="34acf6ef-662a-5766-8123-d77f9d0e2f6f",
    key="FUT20",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SobbleontheBall.Name",
    display_name="Sobble on the Ball",
    searchable_by=["Sobble on the Ball", "Basic", "SobbleontheBall"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="FUT20",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=816,
    abilities=[
        Attack(
            title="Spectacular Save",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Rain Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)