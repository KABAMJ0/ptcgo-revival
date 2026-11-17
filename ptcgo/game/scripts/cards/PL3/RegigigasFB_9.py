from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7932d895-73ff-5415-821d-a5af2e73f2ba",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegigigasFB.Name",
    display_name="Regigigas FB",
    searchable_by=["Regigigas FB", "Basic", "SP", "RegigigasFB"],
    subtypes=["Basic", "SP"],
    collector_number=9,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Attack(
            title="Drain Punch",
            game_text="Remove from Regigigas FB a number of damage counters equal to the amount of Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Lariat",
            game_text="Does 20 damage times the number of different types of Pok\u00e9mon SP you have in play.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)