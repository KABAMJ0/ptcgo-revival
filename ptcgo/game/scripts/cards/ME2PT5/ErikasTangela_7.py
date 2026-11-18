from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39243f1b-300e-5eed-b4d1-113ae4ce34a6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasTangela.Name",
    display_name="Erika's Tangela",
    searchable_by=["Erika's Tangela", "Basic", "ErikasTangela"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Ability(
            title="Gathering of Blossoms",
            game_text="Once during your turn, you may use this Ability. Search your deck for an Erika's Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)