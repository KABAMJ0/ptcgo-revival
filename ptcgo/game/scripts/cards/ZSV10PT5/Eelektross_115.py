from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="925c87f9-6919-5e6a-b904-a6884072a474",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektross.Name",
    display_name="Eelektross",
    searchable_by=["Eelektross", "Stage 2", "Eelektross"],
    subtypes=["Stage 2"],
    collector_number=115,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Thunder Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Buzz Flip",
            game_text="Flip 4 coins. This attack does 100 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)