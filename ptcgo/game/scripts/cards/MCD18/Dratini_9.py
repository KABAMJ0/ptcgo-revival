from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8da26bbe-3e6a-51a6-a9b3-499f1b0ffa38",
    key="MCD18",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    display_name="Dratini",
    searchable_by=["Dratini", "Basic", "Dratini"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="MCD18",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    family_id=147,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for a Dratini, a Dragonair, and a Dragonite, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)