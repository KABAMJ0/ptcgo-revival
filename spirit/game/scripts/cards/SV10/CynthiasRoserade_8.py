from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a16793c5-c0f2-5a56-b3bc-aa4dbc8a7818",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoserade.Name",
    display_name="Cynthia's Roserade",
    searchable_by=["Cynthia's Roserade", "Stage 1", "CynthiasRoserade"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoselia.Name",
    family_id=315,
    abilities=[
        Ability(
            title="Cheer On to Glory",
            game_text="Attacks used by your Cynthia's Pok\u00e9mon do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)