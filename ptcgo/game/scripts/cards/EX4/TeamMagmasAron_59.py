from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cb14385d-6c3a-58da-a63f-626ce59891f8",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAron.Name",
    display_name="Team Magma's Aron",
    searchable_by=["Team Magma's Aron", "Basic", "TeamMagmasAron"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=304,
    abilities=[
        Attack(
            title="Dig Under",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=unimplemented,
        ),
    ],
)