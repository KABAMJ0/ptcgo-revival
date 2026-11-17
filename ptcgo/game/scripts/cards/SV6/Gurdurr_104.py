from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b9e363d3-c48d-579b-9787-d300746e0deb",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    display_name="Gurdurr",
    searchable_by=["Gurdurr", "Stage 1", "Gurdurr"],
    subtypes=["Stage 1"],
    collector_number=104,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Timburr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Knuckle Punch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
        ),
        Attack(
            title="Superpower",
            game_text="You may do 30 more damage. If you do, this Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)