from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cd265bb2-2548-534e-8fdb-7e60545e4068",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasWeepinbell.Name",
    display_name="Erika's Weepinbell",
    searchable_by=["Erika's Weepinbell", "Stage 1", "ErikasWeepinbell"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="ME2PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasBellsprout.Name",
    family_id=69,
    abilities=[
        Attack(
            title="Melt",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title="Leafy Cyclone",
            game_text="During your next turn, this Pok\u00e9mon can't use attacks.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)