from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b440259c-b3fd-57e3-bd85-7103bf83cd76",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tepig.Name",
    display_name="Tepig",
    searchable_by=["Tepig", "Basic", "Tepig"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=498,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
    ],
)