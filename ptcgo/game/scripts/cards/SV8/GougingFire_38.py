from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8b0b7d51-9926-5c28-8c65-020d6c27ac54",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFire.Name",
    display_name="Gouging Fire",
    searchable_by=["Gouging Fire", "Basic", "Ancient", "GougingFire"],
    subtypes=["Basic", "Ancient"],
    collector_number=38,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=1020,
    abilities=[
        Attack(
            title="Lunge Out",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Blazing Charge",
            game_text="If your opponent has 4 or fewer Prize cards remaining, this attack does 70 more damage.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)