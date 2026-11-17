from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2da6b119-e3ea-594a-bf1b-f59785f8bc88",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShellosEastSea.Name",
    display_name="Shellos East Sea",
    searchable_by=["Shellos East Sea", "Basic", "ShellosEastSea"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=422,
    abilities=[
        Attack(
            title="Ripple",
            game_text="Flip a coin. If heads, put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Brine",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any damage counters on it. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)