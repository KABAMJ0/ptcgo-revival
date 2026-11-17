from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0820631b-59c0-5351-b6fc-140b0137b2f6",
    key="MCD12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewott.Name",
    display_name="Dewott",
    searchable_by=["Dewott", "Stage 1", "Dewott"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="MCD12",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oshawott.Name",
    family_id=502,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Razor Shell",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)