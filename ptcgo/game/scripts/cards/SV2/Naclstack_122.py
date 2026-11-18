from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d0d5789-1065-506c-88d3-5d75f7301ed6",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    display_name="Naclstack",
    searchable_by=["Naclstack", "Stage 1", "Naclstack"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    family_id=932,
    abilities=[
        Attack(
            title="Salt Cannon",
            game_text="Flip 3 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)