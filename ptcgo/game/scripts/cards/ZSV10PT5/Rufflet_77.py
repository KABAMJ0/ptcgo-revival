from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f700bf5d-21d3-5727-b1e4-2d328b94f3f5",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic", "Rufflet"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="ZSV10PT5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=627,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)