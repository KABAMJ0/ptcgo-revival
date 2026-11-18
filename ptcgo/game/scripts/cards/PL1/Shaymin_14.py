from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a045d870-7c97-5756-97bf-c836c759b00f",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=492,
    abilities=[
        Attack(
            title="Flower Aroma",
            game_text="Remove 2 damage counters from Shaymin. The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Damage Aid",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 30 damage plus 50 more damage. Then, remove all Special Conditions from the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)