from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ce88a9a-27d4-563d-9064-3b1e61afc5b5",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylGL.Name",
    display_name="Aerodactyl GL",
    searchable_by=["Aerodactyl GL", "Basic", "SP", "AerodactylGL"],
    subtypes=["Basic", "SP"],
    collector_number=55,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=142,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Primal Breath",
            game_text="Your opponent can't play any Pok\u00e9mon from his or her hand to Evolve or to Level-Up the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)