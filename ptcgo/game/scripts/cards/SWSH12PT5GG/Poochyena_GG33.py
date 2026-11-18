from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f25b29fa-ae9a-5458-af7c-9c4d2d03f4a1",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    display_name="Poochyena",
    searchable_by=["Poochyena", "Basic", "Poochyena"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=261,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Slight Intrusion",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)