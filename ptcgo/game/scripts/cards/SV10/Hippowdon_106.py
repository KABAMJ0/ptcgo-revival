from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1cf4354-fc07-59d8-862b-0b10e431f558",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1", "Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
        Attack(
            title="Super Sandstorm",
            game_text="This attack also does 40 damage to each Benched Pok\u00e9mon that has any damage counters on it (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)