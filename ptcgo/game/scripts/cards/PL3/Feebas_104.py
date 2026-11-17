from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="029751f3-48be-5cbd-87a6-fca1b0da4ea1",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="PL3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Count and Draw",
            game_text="Draw a card for each of your opponent's Pok\u00e9mon that isn't an Evolved Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)