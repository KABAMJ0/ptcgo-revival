from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9023dcb-d699-51f5-93d2-c68e33c7b3bc",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic", "Chespin"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Spike Sting",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)