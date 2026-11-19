from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e32b90b0-2121-5d6f-a047-1d4cec3f4dc1",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsZapdosex.Name",
    display_name="Rocket's Zapdos ex",
    searchable_by=["Rocket's Zapdos ex", "Basic", "ex", "RocketsZapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=106,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=145,
    abilities=[
        Ability(
            title="Darkness Guard",
            game_text="As long as Rocket's Zapdos ex has any Darkness Energy attached to it, damage done to Rocket's Zapdos ex by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Plasma",
            game_text="Search your discard pile for a Lightning Energy card and attach it to Rocket's Zapdos ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Raging Thunder",
            game_text="This attack does 30 damage to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)