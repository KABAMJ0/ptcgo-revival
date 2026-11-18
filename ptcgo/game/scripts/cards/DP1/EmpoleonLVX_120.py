from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="455d0357-ff4a-5f58-a454-727eff96bd1d",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EmpoleonLVX.Name",
    display_name="Empoleon LV.X",
    searchable_by=["Empoleon LV.X", "Level-Up", "EmpoleonLVX"],
    subtypes=["Level-Up"],
    collector_number=120,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    family_id=393,
    abilities=[
        Ability(
            title="Supreme Command",
            game_text="Once during your turn (before your attack), you may choose up to 2 cards from your opponent's hand without looking and put them face down next to the Defending Pok\u00e9mon. (These cards are not in play or in your opponent's hand.) At the end of your opponent's next turn, return those cards to your opponent's hand. This power can't be used if Empoleon is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Impact",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 80 damage to that Pok\u00e9mon (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) Empoleon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3},
            effect=unimplemented,
        ),
    ],
)