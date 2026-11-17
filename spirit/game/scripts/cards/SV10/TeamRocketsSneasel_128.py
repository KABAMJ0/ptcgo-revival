from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e44cff16-5fb4-5d29-963e-6efc3bcf70e7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsSneasel.Name",
    display_name="Team Rocket's Sneasel",
    searchable_by=["Team Rocket's Sneasel", "Basic", "TeamRocketsSneasel"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=215,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Strike the Sleeper",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon for each damage counter on that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2},
            effect=unimplemented,
        ),
    ],
)