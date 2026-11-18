from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a0bee81-40c6-5f6b-889d-3e4721d2f04a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name",
    display_name="Simisear",
    searchable_by=["Simisear", "Stage 1", "Simisear"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    family_id=513,
    abilities=[
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)