from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83fd2d13-4870-5ea2-872f-53de79de86b6",
    key="MCD17",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    display_name="Alolan Diglett",
    searchable_by=["Alolan Diglett", "Basic", "AlolanDiglett"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="MCD17",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=50,
    abilities=[
        Attack(
            title="Spelunk",
            game_text="Look at the top 3 cards of your deck and put them back in any order.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
    ],
)