from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ae4f6ce5-6497-526d-975a-6db9ca814241",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    display_name="Team Aqua's Spheal",
    searchable_by=["Team Aqua's Spheal", "Basic", "TeamAquasSpheal"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=363,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Aqua Trance",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
    ],
)