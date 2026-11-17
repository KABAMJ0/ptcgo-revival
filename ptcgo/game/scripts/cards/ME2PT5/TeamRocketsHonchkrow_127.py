from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40835d2f-57b2-5cbb-8be7-e2aa26362c65",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsHonchkrow.Name",
    display_name="Team Rocket's Honchkrow",
    searchable_by=["Team Rocket's Honchkrow", "Stage 1", "TeamRocketsHonchkrow"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMurkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Rocket Feathers",
            game_text="You may discard any number of Supporter cards that have \"Team Rocket\" in their name from your hand, and this attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)