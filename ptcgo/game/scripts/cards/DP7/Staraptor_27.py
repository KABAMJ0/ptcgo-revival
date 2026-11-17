from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cb656c9-c8e9-5817-9337-a51367a83217",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2", "Staraptor"],
    subtypes=["Stage 2"],
    collector_number=27,
    set_code="DP7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Ability(
            title="Protect Wing",
            game_text="As long as Staraptor is your Active Pok\u00e9mon, any damage done by attacks from your opponent's Stage 2 Evolved Pok\u00e9mon is reduced by 20 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Strong Breeze",
            game_text="Flip a coin. If heads, put 1 of your opponent's Benched Pok\u00e9mon and all cards attached to it on top of your opponent's deck. Your opponent shuffles his or her deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=unimplemented,
        ),
    ],
)