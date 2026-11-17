from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="624a8f32-5218-51b3-b1c4-28d71b5719a9",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownK.Name",
    display_name="Unown [K]",
    searchable_by=["Unown [K]", "Basic", "UnownK"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Keep]",
            game_text="Your opponent's attacks, Pok\u00e9mon Powers, and Trainer cards can't discard Energy cards from your Pok\u00e9mon with Unown in their names. (Any other effects still happen.)",
            effect=unimplemented,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)