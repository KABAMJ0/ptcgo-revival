from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a46a509-0e13-5ba8-8a6a-8592019b0df8",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnorlaxLVX.Name",
    display_name="Snorlax LV.X",
    searchable_by=["Snorlax LV.X", "Level-Up", "SnorlaxLVX"],
    subtypes=["Level-Up"],
    collector_number=111,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    family_id=143,
    abilities=[
        Ability(
            title="Big Appetite",
            game_text="Once during your turn (before your attack), if Snorlax is your Active Pok\u00e9mon, you may draw cards until you have 6 cards in your hand. If you do, Snorlax is now Asleep. This power can't be used if Snorlax is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Exercise",
            game_text="You may discard as many Energy cards as you like from your hand. If you do, remove that many damage counters from Snorlax.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=unimplemented,
        ),
    ],
)