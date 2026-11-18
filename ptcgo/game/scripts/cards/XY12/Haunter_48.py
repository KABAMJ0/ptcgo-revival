from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="63ce2727-3958-5b5c-98cb-bc8c5073e0b5",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1", "Haunter"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Dream Eater",
            game_text="If your opponent's Active Pok\u00e9mon is not Asleep, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=unimplemented,
        ),
    ],
)