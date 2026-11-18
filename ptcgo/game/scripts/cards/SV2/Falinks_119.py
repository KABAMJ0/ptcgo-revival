from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="de8e3838-f272-58e9-8176-19dc83476226",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Falinks"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Reckless Charge Together",
            game_text="If Falinks is on your Bench, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)