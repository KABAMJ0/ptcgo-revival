from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="135a688d-091f-55c1-981a-8cb89b42ee20",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    display_name="Galarian Corsola",
    searchable_by=["Galarian Corsola", "Basic", "GalarianCorsola"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=222,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)