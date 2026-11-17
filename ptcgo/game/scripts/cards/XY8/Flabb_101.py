from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db78afed-6d11-530e-b144-e5adb6f0e400",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flabébé",
    searchable_by=["Flab\u00e9b\u00e9", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=669,
    abilities=[
        Attack(
            title="Wish",
            game_text="Flip a coin. If heads, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.FAIRY: 1},
            effect=unimplemented,
        ),
    ],
)