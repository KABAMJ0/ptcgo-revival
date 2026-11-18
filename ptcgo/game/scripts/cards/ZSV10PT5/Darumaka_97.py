from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b133d1dc-99b8-5252-9b5d-8f956969f00d",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    display_name="Darumaka",
    searchable_by=["Darumaka", "Basic", "Darumaka"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Will-O-Wisp",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)