from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="267f9ca8-699e-5d7d-91b9-f36cfb88201d",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name",
    display_name="Trubbish",
    searchable_by=["Trubbish", "Basic", "Trubbish"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=568,
    abilities=[
        Attack(
            title="Acid Spray",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)