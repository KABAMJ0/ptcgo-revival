from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="41666e28-d0bd-56a0-8287-7c86ec681766",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.QuagsireGL.Name",
    display_name="Quagsire GL",
    searchable_by=["Quagsire GL", "Basic", "SP", "QuagsireGL"],
    subtypes=["Basic", "SP"],
    collector_number=76,
    set_code="PL2",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=195,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as Quagsire GL is on your Bench, prevent all damage done to Quagsire GL by attacks (both yours and your opponent's).",
            effect=unimplemented,
        ),
        Attack(
            title="Punch and Run",
            game_text="You may switch Quagsire GL with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)