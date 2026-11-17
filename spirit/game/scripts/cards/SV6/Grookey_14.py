from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c715b80e-d43f-5c4b-8c70-4c6e85543e71",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    display_name="Grookey",
    searchable_by=["Grookey", "Basic", "Grookey"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=810,
    abilities=[
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Branch Poke",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
        ),
    ],
)