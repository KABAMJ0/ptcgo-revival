from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2fed78f9-e1ea-5eb6-a644-a369741a5ecf",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdos.Name",
    display_name="Zapdos",
    searchable_by=["Zapdos", "Basic", "Zapdos"],
    subtypes=["Basic"],
    collector_number=150,
    set_code="PL3",
    rarity=Rarities.RareSecret,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Lightning Burn",
            game_text="Flip a coin. If heads, this attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If tails, Zapdos does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            effect=unimplemented,
        ),
    ],
)