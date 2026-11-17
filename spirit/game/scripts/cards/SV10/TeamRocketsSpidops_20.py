from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e84dd0d8-33ce-5428-8eaf-a87b0b74571c",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsSpidops.Name",
    display_name="Team Rocket's Spidops",
    searchable_by=["Team Rocket's Spidops", "Stage 1", "TeamRocketsSpidops"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsTarountula.Name",
    family_id=917,
    abilities=[
        Ability(
            title="Charging Up",
            game_text="Once during your turn, you may attach a Basic Energy card from your discard pile to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Rocket Rush",
            game_text="This attack does 30 damage for each of your Team Rocket's Pok\u00e9mon in play.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)