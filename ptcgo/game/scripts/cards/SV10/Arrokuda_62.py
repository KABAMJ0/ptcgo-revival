from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d4601a81-9531-5728-868c-7febaed663f6",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    display_name="Arrokuda",
    searchable_by=["Arrokuda", "Basic", "Arrokuda"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=846,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)