from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc033d42-93c3-527e-ab23-6bc6f1d28974",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPonyta.Name",
    display_name="Galarian Ponyta",
    searchable_by=["Galarian Ponyta", "Basic", "GalarianPonyta"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=77,
    abilities=[
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)