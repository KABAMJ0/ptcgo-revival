from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e17f412d-1111-5708-873d-3de2ccb7da17",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Clamperl"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=366,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Clamperl by attacks is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)