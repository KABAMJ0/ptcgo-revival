from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="245c03c5-7463-5e8d-afd9-ffd2816b1a08",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="SV1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=357,
    abilities=[
        Attack(
            title="Fresh-Picked Fruit",
            game_text="Heal 60 damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)