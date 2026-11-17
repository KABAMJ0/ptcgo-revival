from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="77f07519-2a6e-5626-898e-e0c5f368d52e",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesClefairyex.Name",
    display_name="Lillie's Clefairy ex",
    searchable_by=["Lillie's Clefairy ex", "Basic", "ex", "LilliesClefairyex"],
    subtypes=["Basic", "ex"],
    collector_number=56,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=35,
    abilities=[
        Ability(
            title="Fairy Zone",
            game_text="The Weakness of each of your opponent's Dragon Pok\u00e9mon in play is now Psychic. (Apply Weakness as \u00d72.)",
            effect=unimplemented,
        ),
        Attack(
            title="Full Moon Rondo",
            game_text="This attack does 20 more damage for each Benched Pok\u00e9mon (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)