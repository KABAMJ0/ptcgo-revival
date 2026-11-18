from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="42bd74cd-f442-50b9-82d8-cfb2d7aaaf0a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rampardosex.Name",
    display_name="Rampardos ex",
    searchable_by=["Rampardos ex", "Stage 2", "ex", "Rampardosex"],
    subtypes=["Stage 2", "ex"],
    collector_number=100,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cranidos.Name",
    family_id=408,
    abilities=[
        Ability(
            title="Destructive Headbutting",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may use this Ability. Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rowdy Hammer",
            game_text="During your next turn, attacks used by this Pok\u00e9mon do 150 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            cost={PokemonTypes.FIGHTING: 2},
            damage=150,
            effect=unimplemented,
        ),
    ],
)