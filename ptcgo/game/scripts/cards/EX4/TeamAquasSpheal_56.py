from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1d0ddcf-34ce-5f93-8a53-6fa2693701a6",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    display_name="Team Aqua's Spheal",
    searchable_by=["Team Aqua's Spheal", "Basic", "TeamAquasSpheal"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)