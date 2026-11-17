from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8e247b4-0cc9-585e-b642-d2daeb0291a6",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusVSTAR.Name",
    display_name="Arceus VSTAR",
    searchable_by=["Arceus VSTAR", "VSTAR", "ArceusVSTAR"],
    subtypes=["VSTAR"],
    collector_number=70,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusV.Name",
    family_id=493,
    abilities=[
        Ability(
            title="Starbirth",
            game_text="During your turn, you may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. (You can't use more than 1 VSTAR Power in a game.)",
            effect=unimplemented,
        ),
        Attack(
            title="Trinity Nova",
            game_text="Search your deck for up to 3 basic Energy cards and attach them to your Pok\u00e9mon V in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            effect=unimplemented,
        ),
    ],
)