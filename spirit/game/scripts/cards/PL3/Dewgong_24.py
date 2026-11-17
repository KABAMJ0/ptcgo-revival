from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dc49844e-3902-51b7-9c31-cad337d361d4",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Ability(
            title="Thick Fat",
            game_text="Any damage done to Dewgong by attacks from Fire Pok\u00e9mon and Water Pok\u00e9mon is reduced by 30 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Ice Shard",
            game_text="If the Defending Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack's base damage is 80 instead of 30.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)