from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dbeb880a-eb36-5535-8c8c-57a175cbb8b8",
    key="POP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="POP7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=225,
    abilities=[
        Attack(
            title="Present",
            game_text="Flip a coin. If heads, search your deck for any 1 card and put it into your hand. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)