from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2ac180c0-15f3-52a2-bde1-ae0a646e7e1c",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    display_name="Noibat",
    searchable_by=["Noibat", "Basic", "Noibat"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=714,
    abilities=[
        Attack(
            title="Blot",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)