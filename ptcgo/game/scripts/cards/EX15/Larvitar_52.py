from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="be7f7d7e-3adb-5222-a53c-123ef94e3a56",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name",
    display_name="Larvitar δ",
    searchable_by=["Larvitar \u03b4", "Basic", "Larvitar"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="EX15",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=246,
    abilities=[
        Attack(
            title="Paralyzing Gaze",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)