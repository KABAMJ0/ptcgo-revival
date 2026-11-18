from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95b345b3-2ea3-50fc-99e2-5f3ec6e04fd3",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cleffa.Name",
    display_name="Cleffa",
    searchable_by=["Cleffa", "Baby", "Cleffa"],
    subtypes=["Baby"],
    collector_number=48,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=173,
    abilities=[
        Attack(
            title="Energy Recycle",
            game_text="Shuffle a basic Energy card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)