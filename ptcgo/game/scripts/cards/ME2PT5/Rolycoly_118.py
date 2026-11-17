from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="89d4eb12-6876-5d5d-84fa-664fdb704c54",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    display_name="Rolycoly",
    searchable_by=["Rolycoly", "Basic", "Rolycoly"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="ME2PT5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=837,
    abilities=[
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
    ],
)