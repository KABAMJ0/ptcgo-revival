from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea90972e-24a4-52b6-bac6-99b55b13c2d2",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo ★",
    searchable_by=["Mewtwo \u2605", "Basic", "Star", "Mewtwo"],
    subtypes=["Basic", "Star"],
    collector_number=103,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Search your discard pile for an Energy card and attached it to Mewtwo Star.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Star",
            game_text="If the Defending Pok\u00e9mon is an Evolved Pok\u00e9mon, discard all Energy attached to Mewtwo Star and this attack does 50 damage plus 50 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)