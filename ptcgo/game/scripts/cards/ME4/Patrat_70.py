from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3323fb01-906c-51d9-8dc0-1b493ee38562",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    display_name="Patrat",
    searchable_by=["Patrat", "Basic", "Patrat"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=504,
    abilities=[
        Ability(
            title="Watchful Eye",
            game_text="Damage counters on each Pok\u00e9mon (both yours and your opponent's) can't be moved to other Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)