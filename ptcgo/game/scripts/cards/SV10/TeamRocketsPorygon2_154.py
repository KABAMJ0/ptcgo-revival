from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="97a7a6ab-642f-5579-bcf3-2e4d3ab91358",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon2.Name",
    display_name="Team Rocket's Porygon2",
    searchable_by=["Team Rocket's Porygon2", "Stage 1", "TeamRocketsPorygon2"],
    subtypes=["Stage 1"],
    collector_number=154,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPorygon.Name",
    family_id=137,
    abilities=[
        Attack(
            title="R Command",
            game_text="This attack does 20 damage for each Supporter card that has \"Team Rocket\" in its name in your discard pile.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)