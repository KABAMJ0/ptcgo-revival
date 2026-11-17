from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fe08999e-f1f5-5545-906b-a678f9df6778",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="COL",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=16,
    abilities=[
        Attack(
            title="Messenger",
            game_text="Search your deck for a Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle Pidgey and all cards attached to it back into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)