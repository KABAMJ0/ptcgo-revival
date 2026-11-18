from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70c0dc2e-1b2d-5528-92e7-a2b40964104b",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)