from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d4c9998-4172-5df3-9675-9b2301efd224",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSlowbroEX.Name",
    display_name="M Slowbro-EX",
    searchable_by=["M Slowbro-EX", "MEGA", "EX", "MSlowbroEX"],
    subtypes=["MEGA", "EX"],
    collector_number=27,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SlowbroEX.Name",
    family_id=80,
    abilities=[
        Attack(
            title="Loll Roll Spin",
            game_text="This Pok\u00e9mon is now Confused. During your next turn, this Pok\u00e9mon's Loll Roll Spin attack does 100 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)