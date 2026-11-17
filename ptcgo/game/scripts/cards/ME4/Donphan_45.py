from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4e2c97dc-8c84-5cc0-bb82-404481d01632",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="ME4",
    rarity=Rarities.Common,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="No Reprieve",
            game_text="During your next turn, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Smashing Headbutt",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=unimplemented,
        ),
    ],
)