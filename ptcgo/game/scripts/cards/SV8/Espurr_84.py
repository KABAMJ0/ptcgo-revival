from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b7015825-0174-578c-b34b-9fe50b850752",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name",
    display_name="Espurr",
    searchable_by=["Espurr", "Basic", "Espurr"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=677,
    abilities=[
        Attack(
            title="See Through",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)