from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="601d50f1-e502-5b70-a771-c31dd14c5bb2",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic", "Shaymin"],
    subtypes=["Basic"],
    collector_number=38,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=492,
    abilities=[
        Attack(
            title="Energy Blow",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Shaymin.",
            cost={},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Aromatherapy",
            game_text="Remove 2 damage counters from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)