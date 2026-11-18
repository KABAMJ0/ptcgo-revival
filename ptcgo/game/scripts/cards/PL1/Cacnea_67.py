from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f895ae16-cea6-54cb-954d-3f7b8605cd2a",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    display_name="Cacnea",
    searchable_by=["Cacnea", "Basic", "Cacnea"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="PL1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=331,
    abilities=[
        Attack(
            title="Sneaky Attack",
            game_text="If Cacnea has any Darkness Energy attached to it, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Shoot Needle",
            game_text="Flip 2 coins. For each heads, choose 1 of your opponent's Pok\u00e9mon and this attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) (You can choose the same Pok\u00e9mon more than once, but you can't do more than 10 damage to that Pok\u00e9mon in this way.)",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
    ],
)