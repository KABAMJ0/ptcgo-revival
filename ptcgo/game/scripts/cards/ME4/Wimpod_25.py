from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="13a943ae-836d-5f29-aa15-d1501978b07b",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name",
    display_name="Wimpod",
    searchable_by=["Wimpod", "Basic", "Wimpod"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=767,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)