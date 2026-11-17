from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be284a04-d62b-5f9d-803a-748754f8d547",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaGLVX.Name",
    display_name="Dialga G LV.X",
    searchable_by=["Dialga G LV.X", "Level-Up", "SP", "DialgaGLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=122,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DialgaG.Name",
    family_id=483,
    abilities=[
        Ability(
            title="Time Crystal",
            game_text="Each Pok\u00e9mon (both yours and your opponent's) (excluding Pok\u00e9mon SP) can't use any Pok\u00e9-Bodies.",
            effect=unimplemented,
        ),
        Attack(
            title="Remove Lost",
            game_text="Flip a coin until you get tails. For each heads, remove an Energy card attached to the Defending Pok\u00e9mon and put it in the Lost Zone.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)