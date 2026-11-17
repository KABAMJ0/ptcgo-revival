from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccb22093-773a-51a1-b55d-6d90c0ede700",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    display_name="Purrloin",
    searchable_by=["Purrloin", "Basic", "Purrloin"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="RSV10PT5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=509,
    abilities=[
        Attack(
            title="Invite Evil",
            game_text="Search your deck for up to 3 Darkness Pok\u00e9mon, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)