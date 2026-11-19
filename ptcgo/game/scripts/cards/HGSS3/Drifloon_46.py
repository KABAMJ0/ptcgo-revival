from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3041fa1c-df62-5bac-99c8-3879d7a0c013",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    display_name="Drifloon",
    searchable_by=["Drifloon", "Basic", "Drifloon"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="HGSS3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=425,
    abilities=[
        Attack(
            title="Minimize",
            game_text="During your opponent's next turn, any damage done to Drifloon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=protect_next_turn(reduce=20),
        ),
        Attack(
            title="Pull",
            game_text="Flip a coin. If heads, switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)