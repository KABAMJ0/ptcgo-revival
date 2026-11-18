from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8356f357-7406-502d-a2e7-3651ee8a1751",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsAmpharos.Name",
    display_name="Team Rocket's Ampharos",
    searchable_by=["Team Rocket's Ampharos", "Stage 2", "TeamRocketsAmpharos"],
    subtypes=["Stage 2"],
    collector_number=74,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsFlaaffy.Name",
    family_id=179,
    abilities=[
        Ability(
            title="Darkest Impulse",
            game_text="Whenever your opponent plays a Pok\u00e9mon from their hand to evolve 1 of their Pok\u00e9mon, put 4 damage counters on that Pok\u00e9mon. The effect of Darkest Impulse doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Head Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)