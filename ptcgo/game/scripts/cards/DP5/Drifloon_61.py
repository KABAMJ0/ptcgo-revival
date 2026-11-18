from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="926169cd-2f13-511e-822b-c6b248d145c1",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=425,
    abilities=[
        Attack(
            title="Delivery",
            game_text="Flip a coin. If heads, put any 1 card from your discard pile into your hand.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Reaction",
            game_text="Switch Drifloon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)