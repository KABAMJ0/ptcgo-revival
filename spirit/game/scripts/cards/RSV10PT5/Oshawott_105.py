from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="85989668-797b-5222-817c-3e3a5a7e3dac",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    display_name="Oshawott",
    searchable_by=["Oshawott", "Basic", "Oshawott"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=501,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)