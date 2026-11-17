from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="97915638-8cea-50e2-8776-86343134fb4f",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayGLLVX.Name",
    display_name="Luxray GL LV.X",
    searchable_by=["Luxray GL LV.X", "Level-Up", "SP", "LuxrayGLLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=109,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LuxrayGL.Name",
    family_id=405,
    abilities=[
        Ability(
            title="Bright Look",
            game_text="Once during your turn (before your attack), when you put Luxray GL LV.X from your hand onto your Active Luxray GL, you may switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Flash Impact",
            game_text="Does 30 damage to 1 of your Pok\u00e9mon, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)