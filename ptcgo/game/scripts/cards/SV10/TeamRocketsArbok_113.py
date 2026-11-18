from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_all_opponents
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a447af6-a1b6-51c5-bc9b-7d0dad0b9add",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsArbok.Name",
    display_name="Team Rocket's Arbok",
    searchable_by=["Team Rocket's Arbok", "Stage 1", "TeamRocketsArbok"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsEkans.Name",
    family_id=23,
    abilities=[
        Ability(
            title="Potent Glare",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't play any Pok\u00e9mon that has an Ability from their hand, except for Team Rocket's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Spinning Tail",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 3},
            effect=damage_all_opponents(30),
        ),
    ],
)