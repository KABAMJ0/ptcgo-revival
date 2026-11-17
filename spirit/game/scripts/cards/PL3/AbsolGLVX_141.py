from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2771cdd0-0b40-56ca-b916-1f599ebf70d4",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AbsolGLVX.Name",
    display_name="Absol G LV.X",
    searchable_by=["Absol G LV.X", "Level-Up", "SP", "AbsolGLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=141,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AbsolG.Name",
    family_id=359,
    abilities=[
        Ability(
            title="Darkness Send",
            game_text="Once during your turn (before your attack), when you put Absol G LV.X from your hand onto your Active Absol G, you may flip 3 coins. For each heads, put the top card from your opponent's deck in the Lost Zone.",
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Slugger",
            game_text="You may discard a card from your hand. If you do, this attack does 30 damage plus 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)