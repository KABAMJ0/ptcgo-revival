from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea3725e7-9c42-540b-a4dc-e23fb99c8d81",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Appletun.Name",
    display_name="Appletun",
    searchable_by=["Appletun", "Stage 1", "Appletun"],
    subtypes=["Stage 1"],
    collector_number=211,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Applin.Name",
    family_id=840,
    abilities=[
        Attack(
            title="Melting Sweetness",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Tackle",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1},
            damage=130,
            effect=unimplemented,
        ),
    ],
)