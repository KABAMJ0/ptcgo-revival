from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7c6e2f0c-eae6-594f-a823-a7a6a9a1b284",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    display_name="Vibrava",
    searchable_by=["Vibrava", "Stage 1", "Vibrava"],
    subtypes=["Stage 1"],
    collector_number=206,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Trapinch.Name",
    family_id=328,
    abilities=[
        Attack(
            title="Screech",
            game_text="During your next turn, the Defending Pok\u00e9mon takes 50 more damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)