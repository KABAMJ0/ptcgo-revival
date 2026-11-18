from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9b87e565-39e0-5235-b61d-f5a5e552b06f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrio.Name",
    display_name="Wugtrio",
    searchable_by=["Wugtrio", "Stage 1", "Wugtrio"],
    subtypes=["Stage 1"],
    collector_number=57,
    set_code="SV1",
    rarity=Rarities.Uncommon,
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