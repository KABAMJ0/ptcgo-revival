from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1881018-07f8-5f55-84b6-ec23689d635e",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    display_name="Bramblin",
    searchable_by=["Bramblin", "Basic", "Bramblin"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=946,
    abilities=[
        Attack(
            title="Blot",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)