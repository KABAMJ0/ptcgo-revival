from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3fda087-8c0e-5389-b8c8-ab1f1ceda0e5",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    display_name="Sizzlipede",
    searchable_by=["Sizzlipede", "Basic", "Sizzlipede"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=850,
    abilities=[
        Attack(
            title="Heat Dive",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)