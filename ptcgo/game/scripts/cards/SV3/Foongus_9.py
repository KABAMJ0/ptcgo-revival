from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="84373d4d-517e-5354-ae93-1ffcee9cf031",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    display_name="Foongus",
    searchable_by=["Foongus", "Basic", "Foongus"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=590,
    abilities=[
        Attack(
            title="Enticing Pattern",
            game_text="Search your deck for a Basic Grass Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)