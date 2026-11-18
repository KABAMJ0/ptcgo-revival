from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3374bac7-3f5b-5b08-9d30-04b93205e41e",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    display_name="Litten",
    searchable_by=["Litten", "Basic", "Litten"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=725,
    abilities=[
        Attack(
            title="Fake Out",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)