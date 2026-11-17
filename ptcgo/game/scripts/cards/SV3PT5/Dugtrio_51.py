from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="55cfe7e9-4276-59fb-82ef-a21533ff922b",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name",
    display_name="Dugtrio",
    searchable_by=["Dugtrio", "Stage 1", "Dugtrio"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name",
    family_id=50,
    abilities=[
        Attack(
            title="Headbutt Bounce",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Mud Bomb",
            cost={PokemonTypes.FIGHTING: 2},
            damage=80,
        ),
    ],
)