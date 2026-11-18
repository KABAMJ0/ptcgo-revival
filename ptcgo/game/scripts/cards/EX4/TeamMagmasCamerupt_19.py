from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e7bed09-cf6c-5b12-b01e-6a10bbeb1ddb",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasCamerupt.Name",
    display_name="Team Magma's Camerupt",
    searchable_by=["Team Magma's Camerupt", "Stage 1", "TeamMagmasCamerupt"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Overheat",
            game_text="Once during your turn (before your attack), you may search your discard pile for a basic Energy card and attach it to Team Magma's Camerupt. Put 2 damage counters on Team Mamga's Camerupt. This power can't be used if Team Magma's Camerupt is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Flame Ball",
            game_text="You may move a Fire Energy card attached to Team Magma's Camerupt to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)