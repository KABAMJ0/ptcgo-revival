from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="39cd653f-7fac-5132-bdf2-cb5913754a6b",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Root Protector",
            game_text="Any damage done to Swampert by attacks from your opponent's Pok\u00e9mon that isn't an Evolved Pok\u00e9mon is reduced by 20 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Drag Off",
            game_text="Before doing damage, you may switch your opponent's Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Push Over",
            game_text="Does 60 damage plus 10 more damage for each Fighting Energy attached to Swampert.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)