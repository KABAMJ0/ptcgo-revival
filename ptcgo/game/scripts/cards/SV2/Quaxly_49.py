from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0d3a8d29-d73c-55db-9fc9-ffa714303c4f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quaxly.Name",
    display_name="Quaxly",
    searchable_by=["Quaxly", "Basic", "Quaxly"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=912,
    abilities=[
        Attack(
            title="Apply Gel",
            game_text="During your opponent's next turn, if the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)