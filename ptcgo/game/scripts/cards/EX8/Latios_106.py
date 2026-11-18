from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="14aee23b-35f0-5da5-b738-e16c0b3aef1d",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name",
    display_name="Latios ★",
    searchable_by=["Latios \u2605", "Basic", "Star", "Latios"],
    subtypes=["Basic", "Star"],
    collector_number=106,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    family_id=381,
    abilities=[
        Attack(
            title="Miraculous Light",
            game_text="Remove 1 damage counter and all Special Conditions from Latios Star.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Shining Star",
            game_text="If the Defending Pok\u00e9mon is a Stage 2 Evolved Pok\u00e9mon, discard all Energy cards attached to Latios Star and this attack does 50 damage plus 100 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)