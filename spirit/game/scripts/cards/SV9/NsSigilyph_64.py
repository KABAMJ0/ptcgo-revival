from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6aaa3867-ccfd-57a4-8238-97d89763a044",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsSigilyph.Name",
    display_name="N's Sigilyph",
    searchable_by=["N's Sigilyph", "Basic", "NsSigilyph"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=561,
    abilities=[
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Victory Symbol",
            game_text="If you use this attack when you have exactly 1 Prize card remaining, you win this game.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)