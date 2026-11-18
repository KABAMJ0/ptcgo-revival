from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29778367-60e7-549a-83b9-f14d243b63b4",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RagingBolt.Name",
    display_name="Raging Bolt",
    searchable_by=["Raging Bolt", "Basic", "Ancient", "RagingBolt"],
    subtypes=["Basic", "Ancient"],
    collector_number=111,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    abilities=[
        Attack(
            title="Thunderburst Storm",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Headbutt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)