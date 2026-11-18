from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="55547d21-20f8-5c78-8dae-9594715f77d9",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=529,
    abilities=[
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)