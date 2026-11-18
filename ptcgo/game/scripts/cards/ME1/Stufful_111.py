from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6c63ecd6-7ced-5762-9e04-bd98813fb8ea",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    display_name="Stufful",
    searchable_by=["Stufful", "Basic", "Stufful"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=759,
    abilities=[
        Attack(
            title="Light Punch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)