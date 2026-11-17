from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be5b16f5-2943-537f-b351-3546df61a896",
    key="SM35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningMew.Name",
    display_name="Shining Mew",
    searchable_by=["Shining Mew", "Basic", "ShiningMew"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SM35",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Legendary Guidance",
            game_text="Search your deck for up to 2 Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)