from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa3176f0-3ce1-5a3a-b21e-00d904f532cc",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosWattrel.Name",
    display_name="Iono's Wattrel",
    searchable_by=["Iono's Wattrel", "Basic", "IonosWattrel"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=940,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)