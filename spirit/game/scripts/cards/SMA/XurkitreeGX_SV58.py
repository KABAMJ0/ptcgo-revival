from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="28b2c49c-74da-5bfc-847e-bebb3df3efdc",
    key="SMA",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.XurkitreeGX.Name",
    display_name="Xurkitree-GX",
    searchable_by=["Xurkitree-GX", "Basic", "GX", "Ultra Beast", "XurkitreeGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=58,
    set_code="SMA",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=796,
    abilities=[
        Ability(
            title="Flashing Head",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have any Special Energy attached to them.",
            effect=unimplemented,
        ),
        Attack(
            title="Rumbling Wires",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
        Attack(
            title="Lighting-GX",
            game_text="Your opponent reveals their hand. Add a card you find there to their Prize cards face down. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=unimplemented,
        ),
    ],
)