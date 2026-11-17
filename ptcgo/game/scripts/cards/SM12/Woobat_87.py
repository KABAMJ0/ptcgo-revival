from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3ebcc569-1f9c-5ac5-b107-6d529bbcc8e7",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    display_name="Woobat",
    searchable_by=["Woobat", "Basic", "Woobat"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=527,
    abilities=[
        Attack(
            title="Nasal Suction",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Air Cutter",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)