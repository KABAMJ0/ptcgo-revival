from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e839b3f0-a077-52af-b07a-ff1c0aa2a089",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WeavileG.Name",
    display_name="Weavile G",
    searchable_by=["Weavile G", "Basic", "SP", "WeavileG"],
    subtypes=["Basic", "SP"],
    collector_number=17,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=461,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for up to 2 basic Pok\u00e9mon SP and put them onto your Bench. Shuffle your deck afterward.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Team Attack",
            game_text="Does 10 damage plus 10 more damage for each Pok\u00e9mon SP you have in play.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)