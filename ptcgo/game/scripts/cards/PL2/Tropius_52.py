from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="467b63c5-3df7-5aeb-a980-9328acd5a3a9",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tropius.Name",
    display_name="Tropius",
    searchable_by=["Tropius", "Basic", "Tropius"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=357,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, prevent all effects of an attack, including damage, done to Tropius during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Blessed Fruit",
            game_text="Remove all damage counters from 1 of your Benched Grass Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)