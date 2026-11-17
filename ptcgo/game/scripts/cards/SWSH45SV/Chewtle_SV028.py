from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8ae1c35-a4de-5866-98c7-3136b6486c97",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chewtle.Name",
    display_name="Chewtle",
    searchable_by=["Chewtle", "Basic", "Chewtle"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=833,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)