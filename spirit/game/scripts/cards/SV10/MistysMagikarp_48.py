from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62fc1153-8eff-57de-ab01-055114159b38",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysMagikarp.Name",
    display_name="Misty's Magikarp",
    searchable_by=["Misty's Magikarp", "Basic", "MistysMagikarp"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Ability(
            title="So Submerged",
            game_text="As long as this Pok\u00e9mon is on your Bench, prevent all damage from and effects of attacks from your opponent's Pok\u00e9mon done to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)