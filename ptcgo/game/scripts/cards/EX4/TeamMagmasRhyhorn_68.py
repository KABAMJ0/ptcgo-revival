from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f8ce9e63-fc2d-5634-8e66-8a47ba323f4f",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhyhorn.Name",
    display_name="Team Magma's Rhyhorn",
    searchable_by=["Team Magma's Rhyhorn", "Basic", "TeamMagmasRhyhorn"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=111,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)