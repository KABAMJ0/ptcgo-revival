from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d93031f3-5da5-5fd0-a247-64097d7fc39c",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name",
    display_name="Doduo",
    searchable_by=["Doduo", "Basic", "Doduo"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV3PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=84,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)