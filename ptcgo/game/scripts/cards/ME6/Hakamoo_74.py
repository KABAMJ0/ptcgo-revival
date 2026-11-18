from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8ce317e8-f302-5f88-a846-614fedfadc9d",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    display_name="Hakamo-o",
    searchable_by=["Hakamo-o", "Stage 1", "Hakamoo"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="ME6",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jangmoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Double Smash",
            game_text="Flip 2 coins. This attack does 70 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)