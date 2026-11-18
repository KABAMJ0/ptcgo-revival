from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="18894147-f7a9-5522-a0aa-3d9b2287b5be",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    display_name="Shroodle",
    searchable_by=["Shroodle", "Basic", "Shroodle"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=944,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)