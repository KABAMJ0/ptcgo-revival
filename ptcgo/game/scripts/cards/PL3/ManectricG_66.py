from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f06a2c39-b917-5117-8cc9-e6d73e2faed1",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManectricG.Name",
    display_name="Manectric G",
    searchable_by=["Manectric G", "Basic", "SP", "ManectricG"],
    subtypes=["Basic", "SP"],
    collector_number=66,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=310,
    abilities=[
        Attack(
            title="Energy Absorption",
            game_text="Search your discard pile for up to 2 Energy cards and attach them to Manectric G.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)