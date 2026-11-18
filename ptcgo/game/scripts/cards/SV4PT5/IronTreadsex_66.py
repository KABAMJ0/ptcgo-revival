from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e0a5f35-d353-5d42-b9ca-d17f3289736d",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreadsex.Name",
    display_name="Iron Treads ex",
    searchable_by=["Iron Treads ex", "Basic", "ex", "Future", "IronTreadsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=66,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=990,
    abilities=[
        Attack(
            title="Iron-Clad Roll",
            game_text="After doing damage, you may discard all Future Booster Energy Capsules from this Pok\u00e9mon. If you do, during your opponent's next turn, this Pok\u00e9mon takes 150 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=unimplemented,
        ),
    ],
)