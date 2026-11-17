from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a7cb2bb-f0b8-561f-8184-08c11cfa4e14",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX12",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Ability(
            title="Pattern Distraction",
            game_text="As long as Spinda is your Active Pok\u00e9mon, whenever your opponent's Basic Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack does nothing. You can't use more than 1 Pattern Distraction Pok\u00e9-Body each turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Whimsy Draw",
            game_text="Flip a coin until you get tails. For each heads, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Flip a coin. If tails, Spinda does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)