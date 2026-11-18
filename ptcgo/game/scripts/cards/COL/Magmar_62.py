from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="257e3a7e-d027-58e3-bd75-c2d2f44457d0",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name",
    display_name="Magmar",
    searchable_by=["Magmar", "Basic", "Magmar"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="COL",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=126,
    abilities=[
        Attack(
            title="Live Coal",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Magma Punch",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)