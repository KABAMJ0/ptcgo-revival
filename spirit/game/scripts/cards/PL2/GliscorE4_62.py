from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ec41f9b7-fd7d-51b5-b310-e0815ab0e0b5",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GliscorE4.Name",
    display_name="Gliscor E4",
    searchable_by=["Gliscor E4", "Basic", "SP", "GliscorE4"],
    subtypes=["Basic", "SP"],
    collector_number=62,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=472,
    abilities=[
        Attack(
            title="Irongrip",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Loaded Needle",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)