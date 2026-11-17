from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ae52219-b246-5494-83fc-c56aa63c6501",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    display_name="Snivy",
    searchable_by=["Snivy", "Basic", "Snivy"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=495,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)