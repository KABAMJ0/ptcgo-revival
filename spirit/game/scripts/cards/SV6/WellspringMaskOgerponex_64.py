from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="34b5a99c-d946-54df-a4ed-5ec7f78eea05",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WellspringMaskOgerponex.Name",
    display_name="Wellspring Mask Ogerpon ex",
    searchable_by=["Wellspring Mask Ogerpon ex", "Basic", "Tera", "ex", "WellspringMaskOgerponex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=64,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Sob",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Torrential Pump",
            game_text="You may shuffle 3 Energy attached to this Pok\u00e9mon into your deck. If you do, this attack also does 120 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)