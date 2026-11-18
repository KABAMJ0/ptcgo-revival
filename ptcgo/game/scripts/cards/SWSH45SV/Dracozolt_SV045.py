from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7241cb57-6c48-58b7-91c4-a07f2a1126f2",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dracozolt.Name",
    display_name="Dracozolt",
    searchable_by=["Dracozolt", "Stage 1", "Dracozolt"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RareFossil.Name",
    family_id=880,
    abilities=[
        Attack(
            title="Amping Up",
            game_text="During your next turn, this Pok\u00e9mon's Amping Up attack does 90 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=unimplemented,
        ),
    ],
)