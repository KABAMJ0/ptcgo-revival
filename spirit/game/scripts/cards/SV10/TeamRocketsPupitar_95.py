from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3cb8effe-c53d-56cd-8969-e79459c6a5b1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsPupitar.Name",
    display_name="Team Rocket's Pupitar",
    searchable_by=["Team Rocket's Pupitar", "Stage 1", "TeamRocketsPupitar"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsLarvitar.Name",
    family_id=246,
    abilities=[
        Attack(
            title="Explosive Ascension",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)