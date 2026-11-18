from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="961c5de5-9171-58cf-8d9b-fb48fef10354",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    display_name="Silicobra",
    searchable_by=["Silicobra", "Basic", "Silicobra"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=843,
    abilities=[
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)