from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8254e546-5e70-52f4-9c28-d6e00ca4b2e2",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatRotom.Name",
    display_name="Heat Rotom",
    searchable_by=["Heat Rotom", "Basic", "HeatRotom"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=479,
    abilities=[
        Attack(
            title="Heat Tackle",
            game_text="This Pok\u00e9mon also does 40 damage to itself.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)