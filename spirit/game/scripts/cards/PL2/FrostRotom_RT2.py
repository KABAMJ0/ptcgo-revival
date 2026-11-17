from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b6875345-c4c2-55e8-ad58-5108a762fc93",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FrostRotom.Name",
    display_name="Frost Rotom",
    searchable_by=["Frost Rotom", "Basic", "FrostRotom"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    family_id=479,
    abilities=[
        Ability(
            title="Frost Shift",
            game_text="Once during your turn (before your attack), you may use this power. Frost Rotom's type is Water until the end of your turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Hail",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Crushing Ice",
            game_text="Does 40 damage plus 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost (after applying effects to the Retreat Cost).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)