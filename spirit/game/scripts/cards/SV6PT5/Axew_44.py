from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a296c52-9da5-51bc-ad68-8c72bc7e0ce8",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SV6PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=610,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=30,
        ),
    ],
)