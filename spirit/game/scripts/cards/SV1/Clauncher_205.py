from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a2f9297e-cfea-5554-b4b3-3f001f18472d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name",
    display_name="Clauncher",
    searchable_by=["Clauncher", "Basic", "Clauncher"],
    subtypes=["Basic"],
    collector_number=205,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=692,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)