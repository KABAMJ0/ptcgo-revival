from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="92d1b202-98b5-56f1-bc1f-58d61e1eed04",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "Tera", "ex", "Pikachuex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=247,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Ability(
            title="Resolute Heart",
            game_text="If this Pok\u00e9mon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10.",
            effect=unimplemented,
        ),
        Attack(
            title="Topaz Bolt",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=300,
            effect=unimplemented,
        ),
    ],
)