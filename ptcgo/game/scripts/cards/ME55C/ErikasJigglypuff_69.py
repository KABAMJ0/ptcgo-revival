from ptcgo.game.data_utils import PokemonCardDef, Attack, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="877337a4-6f48-5ff6-b450-42f023084966",
    key="ME55C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasJigglypuff.Name",
    display_name="Erika's Jigglypuff",
    searchable_by=["Erika's Jigglypuff", "Basic", "ErikasJigglypuff"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="ME55C",
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
