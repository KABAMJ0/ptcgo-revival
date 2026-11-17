from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6f05bd1a-6517-578f-86b9-884a02974006",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Xurkitree.Name",
    display_name="Xurkitree",
    searchable_by=["Xurkitree", "Basic", "Ultra Beast", "Xurkitree"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=70,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=796,
    abilities=[
        Attack(
            title="Three Mirrors",
            game_text="If your opponent has exactly 3 Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Signal Beam",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)