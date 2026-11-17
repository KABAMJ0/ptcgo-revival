from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4bb0a238-4d32-585e-9795-64dbc2f057db",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronLeavesex.Name",
    display_name="Iron Leaves ex",
    searchable_by=["Iron Leaves ex", "Basic", "ex", "Future", "IronLeavesex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=186,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1010,
    abilities=[
        Ability(
            title="Rapid Vernier",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may switch it with your Active Pok\u00e9mon. If you do, you may move any amount of Energy from your other Pok\u00e9mon to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Prism Edge",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=unimplemented,
        ),
    ],
)