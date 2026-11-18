from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7b2612fe-f55b-5803-9f5a-cc137d956528",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic", "Staryu"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Ability(
            title="Core Guard",
            game_text="If Staryu has any Psychic Energy attached to it, damage done to Staryu by any attack is reduced by 10 (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Pound",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)