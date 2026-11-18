from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7d1a144-0a5c-57bc-9c6d-974d5dc46c62",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smoochum.Name",
    display_name="Smoochum",
    searchable_by=["Smoochum", "Basic", "Smoochum"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=238,
    abilities=[
        Attack(
            title="Delightful Kiss",
            game_text="Search your deck for up to 2 Basic Psychic Energy cards and attach them to 1 of your Benched Pok\u00e9mon. Then, shuffle your deck.",
            cost={},
            effect=unimplemented,
        ),
    ],
)