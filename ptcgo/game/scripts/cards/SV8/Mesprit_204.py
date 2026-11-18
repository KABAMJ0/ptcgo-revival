from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d86c3f92-a610-5886-9f5a-2067b2b1b8ad",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    display_name="Mesprit",
    searchable_by=["Mesprit", "Basic", "Mesprit"],
    subtypes=["Basic"],
    collector_number=204,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=481,
    abilities=[
        Attack(
            title="Full Heart",
            game_text="Attach up to 2 Basic Psychic Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Guardian Burst",
            game_text="If you don't have Uxie and Azelf on your Bench, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)