from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="db05143b-0a13-5a1f-a7b7-a3d6838876d0",
    key="XYP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGengarEX.Name",
    display_name="M Gengar-EX",
    searchable_by=["M Gengar-EX", "MEGA", "EX", "MGengarEX"],
    subtypes=["MEGA", "EX"],
    collector_number=166,
    set_code="XYP",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name",
    family_id=94,
    abilities=[
        Attack(
            title="Hollow Geist",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)