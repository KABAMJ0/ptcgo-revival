from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="462924c0-21bc-5885-9eb6-33ca5388d470",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drizzile.Name",
    display_name="Drizzile",
    searchable_by=["Drizzile", "Stage 1", "Drizzile"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sobble.Name",
    family_id=816,
    abilities=[
        Attack(
            title="Double Stab",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)