from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6bf5db8-2448-5122-9ccc-6db0d0cc75ca",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompCLVX.Name",
    display_name="Garchomp C LV.X",
    searchable_by=["Garchomp C LV.X", "Level-Up", "SP", "GarchompCLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=145,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompC.Name",
    family_id=445,
    abilities=[
        Ability(
            title="Healing Breath",
            game_text="Once during your turn (before your attack), when you put Garchomp C LV.X from your hand onto your Active Garchomp C, you may remove all damage counters from each of your Pok\u00e9mon SP.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Rush",
            game_text="Discard 2 Energy attached to Garchomp C. Choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Garchomp C can't use Dragon Rush during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)