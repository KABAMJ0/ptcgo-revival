from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fa1a899f-b514-5fa2-a9c8-3bd966b0d3fd",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latiasex.Name",
    display_name="Latias ex",
    searchable_by=["Latias ex", "Basic", "ex", "Latiasex"],
    subtypes=["Basic", "ex"],
    collector_number=76,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=380,
    abilities=[
        Ability(
            title="Skyliner",
            game_text="Your Basic Pok\u00e9mon in play have no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Eon Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)