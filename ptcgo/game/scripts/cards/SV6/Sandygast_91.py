from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8311977d-9989-580c-b9ef-a39c57fa7400",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    display_name="Sandygast",
    searchable_by=["Sandygast", "Basic", "Sandygast"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=769,
    abilities=[
        Attack(
            title="Sand Attack",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to use an attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)