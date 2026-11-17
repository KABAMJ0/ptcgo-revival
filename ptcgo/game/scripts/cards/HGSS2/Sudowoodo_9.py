from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b993c3c8-b24f-52b5-a739-c1af7a20c51a",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Push Over",
            game_text="Does 20 damage times the amount of Fighting Energy attached to Sudowoodo.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Rumble",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=unimplemented,
        ),
    ],
)