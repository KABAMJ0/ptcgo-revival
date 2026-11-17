from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="65f85e12-a07d-5e24-b7ac-69c859138ba1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name",
    display_name="Zigzagoon",
    searchable_by=["Zigzagoon", "Basic", "Zigzagoon"],
    subtypes=["Basic"],
    collector_number=167,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=263,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)