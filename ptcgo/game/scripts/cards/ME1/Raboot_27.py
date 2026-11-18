from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c7083ba9-0365-50fd-b3da-aa45012d7eb7",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    display_name="Raboot",
    searchable_by=["Raboot", "Stage 1", "Raboot"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="ME1",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scorbunny.Name",
    family_id=813,
    abilities=[
        Attack(
            title="Jumping Kick",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)