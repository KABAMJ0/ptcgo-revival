from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="024d1c1e-22ad-5830-a8ee-e036af6c8317",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsEnteiex.Name",
    display_name="Rocket's Entei ex",
    searchable_by=["Rocket's Entei ex", "Basic", "ex", "RocketsEnteiex"],
    subtypes=["Basic", "ex"],
    collector_number=97,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Dark Condition",
            game_text="As long as Rocket's Entei ex has any Darkness Energy attached to it, Rocket's Entei ex has no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Link",
            game_text="Search your discard pile for an Energy card and attach it to Rocket's Entei ex.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Volcanic Ash",
            game_text="Discard 2 Energy attached to Rocket's Entei ex and then choose 1 of your opponent's Pok\u00e9mon. This attack does 60 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)