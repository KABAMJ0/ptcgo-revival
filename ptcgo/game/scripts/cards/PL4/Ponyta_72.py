from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e42ad153-4d91-5ebc-8bc2-eccd81447cdc",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name",
    display_name="Ponyta",
    searchable_by=["Ponyta", "Basic", "Ponyta"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="PL4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)