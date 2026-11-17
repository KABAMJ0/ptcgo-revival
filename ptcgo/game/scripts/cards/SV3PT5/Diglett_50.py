from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bd1c829a-885c-54b9-b4ad-93faeae1c1c1",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    display_name="Diglett",
    searchable_by=["Diglett", "Basic", "Diglett"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=50,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)