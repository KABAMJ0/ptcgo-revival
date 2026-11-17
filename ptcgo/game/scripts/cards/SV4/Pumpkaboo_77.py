from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb62e152-5aa8-5adc-8518-1b60cca2bb5e",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic", "Pumpkaboo"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=710,
    abilities=[
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)