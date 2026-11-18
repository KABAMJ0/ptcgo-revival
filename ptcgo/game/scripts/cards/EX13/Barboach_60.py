from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="91bbb91c-68b7-5d8b-99ea-19224c8196c9",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    display_name="Barboach",
    searchable_by=["Barboach", "Basic", "Barboach"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=339,
    abilities=[
        Attack(
            title="Waterfall",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flail",
            game_text="Does 10 damage times the number of damage counters on Barboach.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)