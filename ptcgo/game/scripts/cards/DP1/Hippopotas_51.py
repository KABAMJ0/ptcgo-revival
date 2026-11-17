from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="53432f09-3508-5eb0-b383-85ca92ce0951",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    display_name="Hippopotas",
    searchable_by=["Hippopotas", "Basic", "Hippopotas"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=449,
    abilities=[
        Attack(
            title="Yawn",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Sand Attack",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)