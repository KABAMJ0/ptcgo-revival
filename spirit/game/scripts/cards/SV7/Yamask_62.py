from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d5dcb283-c222-527e-bb63-c4c55591dcf1",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=562,
    abilities=[
        Attack(
            title="Ominous Eyes",
            game_text="Put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=unimplemented,
        ),
    ],
)