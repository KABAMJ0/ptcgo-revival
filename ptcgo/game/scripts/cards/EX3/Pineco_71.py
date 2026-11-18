from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="31042df3-b85c-53fa-839f-a7356002e795",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    display_name="Pineco",
    searchable_by=["Pineco", "Basic", "Pineco"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=204,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="Any damage done to Pineco by attacks is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)