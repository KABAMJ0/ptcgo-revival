from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9c61f009-1910-5c0f-b95d-ca65a561b509",
    key="MCD12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="MCD12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=529,
    abilities=[
        Attack(
            title="Hone ClawsScratch",
            game_text="During your next turn, each of this Pok\u00e9mon's attacks does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1, PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)