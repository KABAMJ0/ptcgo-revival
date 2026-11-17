from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f6b0e098-bcc1-5e0e-b063-388ca18fff76",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina ◇",
    searchable_by=["Giratina \u25c7", "Basic", "Prism Star", "Giratina"],
    subtypes=["Basic", "Prism Star"],
    collector_number=58,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=487,
    abilities=[
        Ability(
            title="Chaotic Star",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may attach 2 Psychic Energy cards from your hand to it.",
            effect=unimplemented,
        ),
        Attack(
            title="Crisis Dive",
            game_text="Discard 2 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=160,
            effect=unimplemented,
        ),
    ],
)