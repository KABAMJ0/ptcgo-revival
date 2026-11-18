from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b6e7442-c57c-5958-8b55-f2b6e8e13adc",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    display_name="Drowzee",
    searchable_by=["Drowzee", "Basic", "Drowzee"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Sleep Inducer",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)