from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26b80363-dc2b-51d8-8bae-c818a5c8a8c7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsOrbeetle.Name",
    display_name="Team Rocket's Orbeetle",
    searchable_by=["Team Rocket's Orbeetle", "Stage 2", "TeamRocketsOrbeetle"],
    subtypes=["Stage 2"],
    collector_number=89,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDottler.Name",
    family_id=824,
    abilities=[
        Ability(
            title="Rocket Brain",
            game_text="As often as you like during your turn, you may move 1 damage counter from 1 of your Team Rocket's Pok\u00e9mon to another of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)