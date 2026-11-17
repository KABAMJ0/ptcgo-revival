from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="394fdc03-dd8e-504d-9658-3f6b7b550ef9",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlang.Name",
    display_name="N's Klang",
    searchable_by=["N's Klang", "Stage 1", "NsKlang"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.NsKlink.Name",
    family_id=599,
    abilities=[
        Attack(
            title="Spinning Gears",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Confront",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)