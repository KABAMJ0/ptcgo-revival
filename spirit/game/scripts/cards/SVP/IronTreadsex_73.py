from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a1ec114-4243-51fd-923e-94df57c2fcc8",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreadsex.Name",
    display_name="Iron Treads ex",
    searchable_by=["Iron Treads ex", "Basic", "ex", "Future", "IronTreadsex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=73,
    set_code="SVP",
    rarity=Rarities.RarePromo,
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