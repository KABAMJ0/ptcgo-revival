from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ee03f4a5-557d-5a86-a733-a8ddc0b12f87",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasJigglypuff.Name",
    display_name="Erika's Jigglypuff",
    searchable_by=["Erika's Jigglypuff", "Basic", "ErikasJigglypuff"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=39,
    abilities=[
        Attack(
            title="Group Therapy",
            game_text="You and your opponent remove 1 damage counter from each of your Pok\u00e9mon with damage counters on them.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Pulled Punch",
            game_text="If the Defending Pok\u00e9mon has no damage counters on it, this attack does 40 damage. If it has any damage counters on it, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="-",
            effect=unimplemented,
        ),
    ],
)