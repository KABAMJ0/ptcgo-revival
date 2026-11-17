from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="918c940f-d411-5a5b-8dad-ce3f55f732d8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=240,
    set_code="SM12",
    rarity=Rarities.RareSecret,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Scatter",
            game_text="At the end of your opponent's turn, if this Pok\u00e9mon has any damage counters on it, flip a coin. If tails, shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)