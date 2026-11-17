from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43e5f074-9e27-5c71-b80b-9607f096fea8",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    display_name="Litleo",
    searchable_by=["Litleo", "Basic", "Litleo"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=667,
    abilities=[
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)