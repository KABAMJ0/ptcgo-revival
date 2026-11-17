from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="11d0d173-9751-5abf-869c-fede8f5c7008",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SteelixGL.Name",
    display_name="Steelix GL",
    searchable_by=["Steelix GL", "Basic", "SP", "SteelixGL"],
    subtypes=["Basic", "SP"],
    collector_number=51,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=208,
    abilities=[
        Attack(
            title="Mend",
            game_text="Search your discard pile for a Metal Energy card and attach it to Steelix GL. If you do, remove 1 damage counter from Steelix GL.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 50 more damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)