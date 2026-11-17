from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38898dee-0151-5410-adfc-6bd1cfbd3ed2",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    display_name="Cutiefly",
    searchable_by=["Cutiefly", "Basic", "Cutiefly"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=742,
    abilities=[
        Attack(
            title="Fly Around",
            game_text="If any damage is done to this Pok\u00e9mon by attacks during your opponent's next turn, flip a coin. If heads, prevent that damage.",
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)