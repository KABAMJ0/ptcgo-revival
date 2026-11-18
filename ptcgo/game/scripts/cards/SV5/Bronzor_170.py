from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ad6c52b8-2f26-5e70-8ecc-09741c1d0d65",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    display_name="Bronzor",
    searchable_by=["Bronzor", "Basic", "Bronzor"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=436,
    abilities=[
        Attack(
            title="Mirror Attack",
            game_text="If your opponent's Active Pok\u00e9mon is a Psychic Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)