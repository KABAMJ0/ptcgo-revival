from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35736834-9962-5c1f-b860-cdb8b8a080d6",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsWeezing.Name",
    display_name="Team Rocket's Weezing",
    searchable_by=["Team Rocket's Weezing", "Stage 1", "TeamRocketsWeezing"],
    subtypes=["Stage 1"],
    collector_number=199,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKoffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Explode Together Now",
            game_text="This attack does 40 damage for each Pok\u00e9mon in play that has \"Koffing\" or \"Weezing\" in its name (both yours and your opponent's).",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)