from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe14d289-6fb4-599f-a1d1-5c476939b6d4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PheromosaGX.Name",
    display_name="Pheromosa-GX",
    searchable_by=["Pheromosa-GX", "Basic", "GX", "Ultra Beast", "PheromosaGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=140,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=795,
    abilities=[
        Attack(
            title="Fast Raid",
            game_text="If you go first, you can use this attack on your first turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Cruel Spike",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Beauty-GX",
            game_text="This attack does 50 damage for each Prize card your opponent has taken. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)