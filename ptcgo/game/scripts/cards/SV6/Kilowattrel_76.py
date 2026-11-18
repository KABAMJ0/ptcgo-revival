from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0a95bc2c-c81a-5d09-a0d6-c2a5ed8790e9",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1", "Kilowattrel"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="SV6",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Wind Power Charge",
            game_text="During your next turn, attacks used by this Pok\u00e9mon do 120 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Strong Volt",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)