from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b53dcf3d-6793-5070-bbcb-c3ac009d0103",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GougingFire.Name",
    display_name="Gouging Fire",
    searchable_by=["Gouging Fire", "Basic", "Ancient", "GougingFire"],
    subtypes=["Basic", "Ancient"],
    collector_number=151,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
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