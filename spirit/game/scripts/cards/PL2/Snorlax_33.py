from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68d2a9ad-20d2-5915-9d5e-ec3e4a96bc34",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Pick and Collect",
            game_text="Search your discard pile for up to 4 basic Energy cards, show them to your opponent, and put them into your hand.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Roll Over",
            game_text="Flip a coin. If heads, both Snorlax and the Defending Pok\u00e9mon are now Asleep. If tails, Snorlax is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            effect=unimplemented,
        ),
    ],
)