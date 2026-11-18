from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f3dbff78-7ea7-590e-8ad4-eab112f53136",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name",
    display_name="Mime Jr.",
    searchable_by=["Mime Jr.", "Basic", "MimeJr"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="SV4PT5",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=439,
    abilities=[
        Attack(
            title="Mimed Games",
            game_text="Your opponent chooses an attack from 1 of their Pok\u00e9mon in play. Use the chosen attack as this attack.",
            cost={},
            effect=unimplemented,
        ),
    ],
)