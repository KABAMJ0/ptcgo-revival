from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a05c9df1-5124-5673-bc2a-52e4ef200468",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HippowdonE4.Name",
    display_name="Hippowdon E4",
    searchable_by=["Hippowdon E4", "Basic", "SP", "HippowdonE4"],
    subtypes=["Basic", "SP"],
    collector_number=42,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=450,
    abilities=[
        Ability(
            title="Sand Armor",
            game_text="If Hippowdon E4 has any Fighting Energy attached to it, any damage done to Hippowdon E4 by attacks is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Bite and Crush",
            game_text="Flip 2 coins. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)