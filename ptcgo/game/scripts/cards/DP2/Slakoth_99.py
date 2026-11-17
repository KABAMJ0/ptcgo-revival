from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5127f790-2e3d-55f2-8e65-70a84c3732cd",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="DP2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Drowsy",
            game_text="Both Slakoth and the Defending Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)