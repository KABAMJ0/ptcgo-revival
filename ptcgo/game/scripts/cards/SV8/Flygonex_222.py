from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45958871-e4a9-5f10-9666-dc106bedbc3f",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygonex.Name",
    display_name="Flygon ex",
    searchable_by=["Flygon ex", "Stage 2", "Tera", "ex", "Flygonex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=222,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=310,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Attack(
            title="Reversing Storm",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Peridot",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon ex and Pok\u00e9mon V. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
    ],
)