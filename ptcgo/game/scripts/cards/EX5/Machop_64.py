from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fcc95beb-f866-51f8-95e0-00204f7af036",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name",
    display_name="Machop",
    searchable_by=["Machop", "Basic", "Machop"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=66,
    abilities=[
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Karate Chop",
            game_text="Does 30 damage minus 10 damage for each damage counter on Machop.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)