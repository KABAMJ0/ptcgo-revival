from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa77f8da-b8af-5fc5-9eac-af41de22ae0e",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScreamTail.Name",
    display_name="Scream Tail",
    searchable_by=["Scream Tail", "Basic", "Ancient", "ScreamTail"],
    subtypes=["Basic", "Ancient"],
    collector_number=77,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=985,
    abilities=[
        Attack(
            title="Supportive Singing",
            game_text="Heal 100 damage from 1 of your Benched Ancient Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)