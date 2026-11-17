from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d8fbfa8-8ce9-51a2-a4a4-17226a606cca",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZLVX.Name",
    display_name="Porygon-Z LV.X",
    searchable_by=["Porygon-Z LV.X", "Level-Up", "PorygonZLVX"],
    subtypes=["Level-Up"],
    collector_number=100,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    family_id=474,
    abilities=[
        Ability(
            title="Mode Crash",
            game_text="Once during your turn (before your attack), when you put Porygon-Z LV.X from your hand onto your Active Porygon-Z, you may discard all of your opponent's Special Energy cards in play.",
            effect=unimplemented,
        ),
        Ability(
            title="Decode",
            game_text="Once during your turn (before your attack), you may search your deck for up to any 2 cards and shuffle your deck afterward. Then, put those cards on top of your deck in any order. This power can't be used if Porygon-Z is affected by a Special Condition.",
            effect=unimplemented,
        ),
    ],
)