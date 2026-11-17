from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="67197b45-c8f7-5738-b57c-4bcaab0ad665",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    display_name="Nosepass",
    searchable_by=["Nosepass", "Basic", "Nosepass"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=299,
    abilities=[
        Ability(
            title="Magnetic Reversal",
            game_text="Once during your turn (before your attack), if Nosepass is your Active Pok\u00e9mon, you may flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. This power can't be used if Nosepass is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)