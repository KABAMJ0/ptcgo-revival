from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6661b650-6e5d-5c0b-a278-be325b550c50",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreonex.Name",
    display_name="Umbreon ex",
    searchable_by=["Umbreon ex", "Stage 1", "Tera", "ex", "Umbreonex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=161,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Moon Mirage",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
        Attack(
            title="Onyx",
            game_text="Discard all Energy from this Pok\u00e9mon, and take a Prize card.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
    ],
)