from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ccab9631-786d-5fcb-a9a4-0084850f773a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulderex.Name",
    display_name="Iron Boulder ex",
    searchable_by=["Iron Boulder ex", "Basic", "ex", "Future", "IronBoulderex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=147,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Attack(
            title="Repulsor Axe",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Power Stomp",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)