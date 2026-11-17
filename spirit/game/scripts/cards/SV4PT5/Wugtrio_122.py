from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="47f71503-b022-5e60-a3ae-1a480e099d7a",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name",
    display_name="Wugtrio",
    searchable_by=["Wugtrio", "Stage 1", "Wugtrio"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Undersea Tunnel",
            game_text="Flip 3 coins. For each heads, discard the top 3 cards of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=unimplemented,
        ),
    ],
)