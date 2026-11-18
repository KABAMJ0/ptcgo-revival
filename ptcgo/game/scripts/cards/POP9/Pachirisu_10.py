from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a07f06cb-8148-50bc-8518-b9a11ee855d3",
    key="POP9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="POP9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=417,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Poison Berry",
            game_text="If you have Croagunk in play, this attack does 20 damage plus 20 more damage and the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)