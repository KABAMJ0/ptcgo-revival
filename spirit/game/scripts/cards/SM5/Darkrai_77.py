from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="407ce2d8-ce50-5543-a1bb-7c4d89ade0bf",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai ◇",
    searchable_by=["Darkrai \u25c7", "Basic", "Prism Star", "Darkrai"],
    subtypes=["Basic", "Prism Star"],
    collector_number=77,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=491,
    abilities=[
        Ability(
            title="Nightmare Star",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach 2 Darkness Energy cards from your hand to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Abyssal Sleep",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. Your opponent flips 2 coins instead of 1 between turns. If either of them is tails, that Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.DARKNESS: 4},
            damage=120,
            effect=unimplemented,
        ),
    ],
)